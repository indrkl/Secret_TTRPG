import streamlit as st
import numpy as np, pandas as pd, itertools as it
from collections import defaultdict, Counter
from scipy.optimize import linear_sum_assignment as lsa
import altair as alt

mnf = lambda o : tuple(np.bincount(o,minlength=7)[1:])
rev_mnf = lambda o: sum([ (i+1,)*n for i,n in enumerate(o)],tuple())

def get_counts(ndice):
    die = list(np.arange(1,7))
    opts = list(it.product( *[die]*ndice ))
    return { rev_mnf(k):v for k,v in dict(Counter(map(mnf,opts))).items() }

def nnudges(target,dice):
    if len(target)>len(dice): return 'impossible'
    dmat = np.abs(np.array(target)[:,None] - np.array(dice)[None,:])
    return dmat[lsa(dmat)].sum()

def get_dist(target,counts):
    dist = defaultdict(lambda: 0)
    for d, c in counts.items():
        dist[nnudges(target,d)] += c

    df = pd.DataFrame({'n':dist.keys(),'c':dist.values()}).sort_values('n')
    df['ns'] = df['n'].astype('str').str.rjust(2)
    df['p'] = df['c']/df['c'].sum()
    df['cp'] = df['p'].cumsum()
    df = df[df['cp']<0.999]
    return df

def plot_dist(ddf):
    p1 = alt.Chart(ddf).mark_bar(size=25).encode(
        x=alt.X('ns',title=f'Nudges for {target}'), y=alt.Y('p',axis=alt.Axis(format='.0%'),title='Probability'),
        			tooltip=[alt.Tooltip('p',format='.1%',title="Probability")])
    p2 = alt.Chart(ddf).mark_bar(size=25).encode(
        x=alt.X('ns',title=f'Nudges for {target}'), y=alt.Y('cp',axis=alt.Axis(format='.0%'),title='Cumulative probability'),
        			tooltip=[alt.Tooltip('cp',format='.1%',title="Cumulative probability")])
    return (p1 | p2)

st.header('Nudge distribution calculator')

ndice = st.number_input('Number of dice',value=6)
target = st.text_input("Target combination 1:",value='3,3,3')
target = tuple(map(int,target.split(',')))

counts = get_counts(ndice)
dist = get_dist(target,counts)
st.write(f"Average number of nudges needed: {(dist['p']*dist['n']).sum():.1f}")
st.altair_chart(plot_dist(dist))

target = st.text_input("Target combination 2:",value='6,6,6')
target = tuple(map(int,target.split(',')))

counts = get_counts(ndice)
dist = get_dist(target,counts)
st.write(f"Average number of nudges needed: {(dist['p']*dist['n']).sum():.1f}")
st.altair_chart(plot_dist(dist))