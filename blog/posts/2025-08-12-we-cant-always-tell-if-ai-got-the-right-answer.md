### We Can't Always Tell if AI Got the Right Answer

I suppose it isn't news to anyone that US President Donald Trump loves tariffs, and that announcements and discussion concerning tariffs have caused all sorts of perturbations across various markets since his election. In this post I'm going to focus on market perturbations surrounding copper tariff-related annoucements and ask: did an AI respond correctly to discussion concerning copper tariffs, without anyone noticing?

#### Background

On 25 February this year, Trump [ordered](https://www.whitehouse.gov/presidential-actions/2025/02/addressing-the-threat-to-nationalsecurity-from-imports-of-copper/) Secretary of Commerce Howard Lutnick to initiate an investigation into the national security implications of copper imports into the United States, under Section 232 of the Trade Expansion Act of 1962. The scope of the investigation was to be maximally broad:

> including but not limited to:
>
> (i)&nbsp;&nbsp;&nbsp;raw mined copper;  
> (ii)&nbsp;&nbsp;copper concentrates;  
> (iii)&nbsp;refined copper;  
> (iv)&nbsp;copper alloys;  
> (v)&nbsp;&nbsp;scrap copper; and  
> (vi)&nbsp;derivative products.

[//]: # ( [authorizes](https://www.bis.doc.gov/index.php/other-areas/office-of-technology-evaluation-ote/section-232-investigations) the US Secretary of Commerce to investigate whether importation of a particular article &lsquo;is in such quantities or under such circumstances as to threaten to impair the national security&rsquo;. In response, the President can &lsquo;adjust the imports of an article and its derivatives&rsquo; if that is deemed necessary. The scope of [the copper investigation](https://www.federalregister.gov/documents/2025/03/13/2025-04061/notice-of-request-for-public-comments-on-section-232-national-security-investigation-of-imports-of) accounced by Commerce Secretary Howard Lutnick was maximally broad: > The Secretary of Commerce has initiated an investigation to determine the effects on U.S. national security of imports of copper in all forms, including, but not limited to, raw mined copper; copper concentrates; refined copper; copper alloys; scrap copper; and derivative products.)

This immediately led to questions concerning potential tariffs or quotas on imports of copper, and the impacts thereof on copper prices. What really set the cat among the pigeons, though, was on 8 July when Trump [remarked](https://www.facebook.com/reel/1641884246475346) during a televised cabinet meeting:

> We did steel as you know, they're 50%, we did aluminum, 50%... And now, today we're doing copper. I believe the tariff on copper, we're going to make it 50%.

Later in the day, Lutnick [confirmed](https://www.reuters.com/business/healthcare-pharmaceuticals/trump-says-he-will-impose-50-tariff-copper-imports-tuesday-2025-07-08/) that the Section 232 Investigation was complete. He said that he expected the tariffs to come into effect by the end of July, adding:

> The idea is to bring copper home, bring copper production home, bring the ability to make copper, which is key to the industrial sector, back home to America.

The comparison with steel and alumin(i)um in Trump's remarks is important, because in those cases the 50% tariff that has been imposed _does_ apply to imports of refined metal. The most natural interpretation of Lutnick's comment about the desire to \`bring copper production home' also strongly implies that refined metal would be in focus: \`copper production' surely includes copper smelting, i.e. the production of refined copper from ores and concentrates.

Needless to say, these announcements had an effect on the price of copper in the United States. Globally, the two largest futures exchanges for copper are the [Chicago Mercantile Exchange](https://www.cmegroup.com/markets/metals/base/copper.settlements.html) and the [London Metal Exchange](https://www.lme.com/en/Metals/Non-ferrous/LME-Copper). Factors other than politicians' announcements can move the copper price, of course, so probably the simplest way to measure the effects of the Section 232 newsflow on the copper price is to look at the  difference between the Chicago (COMEX) and London (LME) prices. That's because metal flowing into warehouses to underpin COMEX contracts would be subject to US import tariffs (the warehouses are in the US), whereas metal underpinning LME contracts wouldn't. The following chart shows the premium of the COMEX copper price over the LME, for August settlement (i.e., the next month after the tariff was expected to come into effect), from the middle of 2024 to the close on 27 July 2025.

<img src="/blog/images/arb_aug_prelim.png" style="max-width:600px;"
alt="COMEX/LME copper arbitrage, August 2025 delivery, July 2024 to 27 July 2025."
/>

As you can see, the COMEX premium never quite got up to 50%, but Trump's statement about how he was \`going to make it 50%' in particular widened the gap substantially. It had already been building since late 2024, as rumours of the Section 232 investigation had been circulating before it was official.

#### An AI Intervention

On 28 July at approximately 10:25 New York time, the following newsflash came through Bloomberg:

> *CHILE FINANCE MINISTER EXPECTS COPPER TARIFF EXCEPTION: EMOL

About 10 minutes later, another newsflash came through:

> *CORRECT: CHILE'S MARCEL HOPES FOR COPPER TARIFF EXCEPTION: EMOL

In the meantime, this is what happened to the COMEX copper price:

<img src="/blog/images/bbgnews.png" style="max-width:600px;"
alt="COMEX copper price, August 2025 delivery, 10:00 to 11:00 on 28 July 2025."
/>

Chile produces the most copper of any country in the world. An exemption for imports from Chile would neutralize any effect of tariffs on the price. It would also rather seem to undermine the goal of \`bringing copper production home'.

The Chilean Minister of Finance, Mario Marcel, had very clearly [said](https://www.emol.com/noticias/Economia/2025/07/28/1173352/mario-marcel-aranceles.html) that he \`hoped' for an exemption:

> Nosotros lo que esperamos es que estas conversaciones que empiezan hoy día en Washington, abarquen también en tema del cobre.
>
> _We hope that these talks, which begin today in Washington, will also cover the issue of copper._

The journalistic gloss of this interview had also described Marcel as \`optimistic' regarding the possibility of an exemption, because he said:

> Para este tipo de materias primas en otros acuerdos, se han hecho excepciones y se han incluido dentro del conjunto de negociaciones.
> 
> _For this type of raw material, exceptions have been made in other agreements and they have been included in the negotiations._

But there was nothing there to justify the description of this hope, or even optimism, as an _expectation_.

So, why had an expectation been reported? The answer came in a Bloomberg news roundup the next day:

<img src="/blog/images/bbg_summary.png" style="max-width:600px;"
alt="Bloomberg News: Goldman says Trump's minerals diplomacy poses copper risks."
/>

Bloomberg's AI had somehow inferred... hallucinated?... that Marcel _expected_ a tariff exemption for Chile. At this point, the moral of the story seemed to be that we all (not least Bloomberg) should learn lessons about over-reliance on AI, and maybe sympathise with anyone who lost money on intra-day trading on 28 July, until...

#### The Twist in the Tail

True to the expected timeframe, Trump made a [proclamation](https://www.whitehouse.gov/presidential-actions/2025/07/adjusting-imports-of-copper-into-the-united-states/) on 30 July on \`adjusting imports of copper into the United States'. However, the substance of the proclamation was _not_ true to expectations:

> the Secretary recommended an immediate universal 30 percent import duty on semi-finished copper products and intensive copper derivative products.  The Secretary also recommended a phased universal tariff on refined copper of 15 percent starting in 2027 and 30 percent starting in 2028.

Refined copper was _not_ going to be subjected to a 50% import tariff after all, or indeed any tariff until 2027 (if then). So, the continuation of the COMEX/LME arbitrage chart above now looks like this:

<img src="/blog/images/arb_aug.png" style="max-width:600px;"
alt="COMEX/LME copper arbitrage, August 2025 delivery, July 2024 to 11 August 2025."
/>

I trust that I don't need to draw any vertical lines on this chart. All that COMEX premium, built up over the space of over six months, was wiped out in one fell swoop.

#### Did the AI Know What Was Coming?

At this point, I feel that we have to ask the question: was the Bloomberg AI, which reported that the Chileans expected an exemption for copper, right?

In one sense, no: there is no specific exemption for Chile. In another sense, yes: imports of refined copper from Chile won't be tariffed. It was _that_ belief that caused the copper price to drop over 3.25% in the space of a minute on 28 July, and _if you had traded on that belief at any point before the big reveal on 30 July, you would have made money_. What more could you want from a financial news AI?

Suppose we accept that the AI was \`right', in the latter sense. Was it right for the right reasons? Had it somehow, reading between the lines in an inscrutable way, understood that Mario Marcel indeed expected Chilean copper not to be subjected to US tariffs? _Did_ Marcel expect that?

Questions like this are going to keep arising as we become more reliant on AIs, because the reasons why they produce the outputs they do are often near-impossible to discern with any certainty: witness the not-very-confidence-inspiring [explanation](https://x.com/grok/status/1943916977481036128) given for what caused Grok to become \`MechaHitler' for a day. I will stick my neck out and say that whatever caused Bloomberg's AI to report that Mario Marcel \`expected' a copper tariff exception for Chile, it's not that it wasn't able to translate \`esperamos'. The explanation must be something else.

<div style="text-align:right;font-style:italic">12 August 2025</div>