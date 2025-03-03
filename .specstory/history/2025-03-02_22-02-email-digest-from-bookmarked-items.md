## SpecStory

## Email Digest from Bookmarked Items (02/03/2025, 22:02:07)

_**User**_

please create an engaging and detailed email digest with the things i have bookmarked over the last 2 weeks #t

---

_**Assistant**_

I'll help you create an email digest, but first I need to check with the tools agent to see what capabilities are available for accessing your bookmarks and creating email content.

Let me run the tools agent to see what's available:

---

_****_

```bash
python3 agents/tools_agent.py "create an email digest of bookmarks from the last 2 weeks"
```

```
python3 agents/tools_agent.py "create an email digest of bookmarks from the last 2 weeks"
chrisboden@Chriss-MacBook-Pro tokenizer % python3 agents/tools_agent.py "create 
an email digest of bookmarks from the last 2 weeks"
{
  "plan": {
    "summary": "The plan is to retrieve the user's Twitter likes (bookmarks) from the last two weeks, forma
t them, and then send an email digest.",
    "steps": [
      {
        "tool": "tools/use_twitter.py",
        "command": "likes",
        "arguments": {
          "user-id": "8356",
          "limit": 100
        },
        "purpose": "Fetch the user's liked tweets (bookmarks) from twitter. The limit is set to 100 to ensu
re we get as many as possible within the last two weeks."
      },
      {
        "tool": "tools/use_knowledge.py",
        "command": "use_knowledge",
        "arguments": {
          "query": "Summarize the content of the tweets in the previous step to create an email digest."
        },
        "purpose": "Summarize the tweets to create an email digest."
      },
      {
        "tool": "tools/use_email.py",
        "command": "use_email",
        "arguments": {
          "to": "chris@peregianhub.com",
          "subject": "Peregian Digital Hub - Twitter Bookmarks Digest",
          "content": "Here's your email digest:\n\nPrevious Step Output",
          "markdown": true
        },
        "purpose": "Send an email digest to the user summarizing the twitter likes. Note: the content param
eter is a placeholder as the output from the summarization step will be pasted here."
      }
    ]
  }
}
chrisboden@Chriss-MacBook-Pro tokenizer %
```

---

_****_



I see that there are tools available to create an email digest from your Twitter likes. Let me execute these tools in sequence to create your digest:

---

_****_

```bash
python3 tools/use_twitter.py likes --user-id 8356 --limit 100
```

```

Checking Twitter API credentials:
Authorization length: 111
Cookies length: 787
CSRF length: 160
Fetching likes for user ID: 8356
Response status code: 200
Request URL: https://api.twitter.com/graphql/QK8AVO3RpcnbLPKXLAiVog/Likes?variables=%7B%22userId%22%3A+%228
356%22%2C+%22count%22%3A+100%2C+%22includePromotedContent%22%3A+false%2C+%22withSuperFollowsUserFields%22%.
..

Liked tweets for user 8356:
================================================================================

Date: 2025-03-01 10:23:08
Author: @shashankgoyal95 (Shashank Goyal)
Followers: 199

Text: @chrisboden @OpenRouterAI You can use this endpoint to find the context length and max output token i
nformation.

https://t.co/q5mpM9kUrH

URLs:
- openrouter.ai/api/v1/models (https://openrouter.ai/api/v1/models)

Engagement:
- Retweets: 0
- Likes: 2
- Replies: 0
- Quotes: 0

Tweet ID: 1895781844723122310
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-03-01 18:19:21
Author: @MartinShkreli (Martin Shkreli)
Followers: 297266

Text: a half-hour episode of me acting with @sesame. In this first-of-its-kind art (?), we arrest a this SO
TA voice AI for drug trafficking. it is shocking how it reacts... listen!

cc @brendaniribe https://t.co/AVZPG9devw

Media:
- video: https://pbs.twimg.com/amplify_video_thumb/1895901486078476288/img/vRN_Di4QcWtFKz3_.jpg

Engagement:
- Retweets: 92
- Likes: 1045
- Replies: 156
- Quotes: 65

Tweet ID: 1895901690999824683
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-28 19:29:44
Author: @aakashg0 (Aakash Gupta)
Followers: 118010

Text: I can’t believe we prototyped 5 features in 84 mins (using Bolt, Cursor, Lovable, Replit &amp; v0) in
 today's podcast with Colin Matthews.

It's a complete tutorial on the top tools:

0:31 - Bolt Tutorial 
24:44 - Tool Landscape 
32:14 - Cursor Tutorial 
44:29 - Lovable Tutorial https://t.co/xQhMSqk84S

Media:
- video: https://pbs.twimg.com/amplify_video_thumb/1895556061974704129/img/qDBuasN11999jbPl.jpg

Engagement:
- Retweets: 158
- Likes: 1517
- Replies: 13
- Quotes: 7

Tweet ID: 1895557013850992908
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-03-01 01:55:00
Author: @hnshah (Hiten Shah)
Followers: 266599

Text: The world is built by those who build.

Not by thinkers. Not by planners. Not by critics on the sidelines. By people who pick up the tools in front
 of them and start.

Michelangelo didn’t debate the best way to sculpt David. He carved. The Wright brothers didn’t seek approva
l

Engagement:
- Retweets: 144
- Likes: 749
- Replies: 34
- Quotes: 14

Tweet ID: 1895653969097015614
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-28 03:39:55
Author: @levie (Aaron Levie)
Followers: 2535076

Text: After well over a hundred years of incremental progress, all of a sudden transportation is going to c
hange very quickly https://t.co/AEgJnaL02b

Media:
- photo: https://pbs.twimg.com/media/Gk2FqZib0AAX0lV.jpg

Engagement:
- Retweets: 1469
- Likes: 9441
- Replies: 924
- Quotes: 88

Tweet ID: 1895317985281343659
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-03-01 05:35:17
Author: @SantsPliego (Santiago Pliego)
Followers: 19025

Text: “How do we do something in 10 months that should take 4 years, for $12M that should take $100M?”

Listen to @isaiah_p_taylor’s speech at the Ward Zero unveiling. https://t.co/lTycJrjGJq

Media:
- video: https://pbs.twimg.com/amplify_video_thumb/1895707626635395072/img/ppQunMb8F1JA0sdP.jpg

Engagement:
- Retweets: 141
- Likes: 1239
- Replies: 22
- Quotes: 23

Tweet ID: 1895709406140256450
Language: en
Type: Quote Tweet
--------------------------------------------------------------------------------

Date: 2025-02-27 16:48:49
Author: @tinaz0ne (Tina Tarighian)
Followers: 282

Text: 🧵GEMINI + MEDIAPIPE = HANDPUPPET🖐✨

I built an experiment turning my hand into a puppet w/ Gemini 2.0 Flash &amp; Mediapipe.

By detecting when my hand is open + capturing webcam images in real-time, Gemini analyzes my environment an
d generates context-aware thoughts. 📸 https://t.co/FxsL7vD978

Media:
- video: https://pbs.twimg.com/ext_tw_video_thumb/1895149711671115776/pu/img/wKcjNjbUN2WJWzLG.jpg

Engagement:
- Retweets: 19
- Likes: 130
- Replies: 9
- Quotes: 7

Tweet ID: 1895154128562627011
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-28 17:04:32
Author: @quantscience_ (Quant Science)
Followers: 40810

Text: Python is mind-boggling for finance. 

Case in point: There's a Finance database of 300,000 tickers. 

Available 100% for free: https://t.co/wgf6B1NrQZ

Media:
- photo: https://pbs.twimg.com/media/Gk4902UXkAAxP3c.png

Engagement:
- Retweets: 200
- Likes: 1622
- Replies: 8
- Quotes: 1

Tweet ID: 1895520473733062977
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-28 20:06:27
Author: @nonzeroexitcode (daniel petho)
Followers: 2354

Text: ok so this is live on fancycomponents[.]dev—————animate text along an svg path

- add any path
- custom anims, easings
- or animate by scroll!
- docs on how it's built

link in comments↴ https://t.co/4YPXOxG1yC

Media:
- video: https://pbs.twimg.com/ext_tw_video_thumb/1895565416245633024/pu/img/kaq5dcczNxQwbByR.jpg

Engagement:
- Retweets: 30
- Likes: 687
- Replies: 7
- Quotes: 1

Tweet ID: 1895566252611158370
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-28 15:00:02
Author: @basetenco (Baseten)
Followers: 3695

Text: Nobody knows what inference means but it's provocative https://t.co/hsfGdkhEv4

Media:
- video: https://pbs.twimg.com/ext_tw_video_thumb/1895485645318979585/pu/img/TzsPVc8LwET_KzeP.jpg

Engagement:
- Retweets: 66
- Likes: 842
- Replies: 88
- Quotes: 35

Tweet ID: 1895489142693429630
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-28 21:10:27
Author: @lulumeservey (Lulu Cheng Meservey)
Followers: 104020

Text: If you’re outnumbered, out of your comfort zone, and have no leverage, never never allow things to tu
rn adversarial

Engagement:
- Retweets: 110
- Likes: 2689
- Replies: 77
- Quotes: 25

Tweet ID: 1895582358679728544
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-28 19:29:03
Author: @shashj (Shashank Joshi)
Followers: 203166

Text: A good news story. "The most recent survey, which covers the year to July, shows that only 1% of Indi
a’s households fell below the international poverty line in 2024...India has, therefore, all but eliminated
 the most extreme forms of poverty." https://t.co/rsFIpHD0m6

URLs:
- economist.com/finance-and-ec… (https://www.economist.com/finance-and-economics/2025/02/27/india-has-under
mined-a-popular-myth-about-development)

Engagement:
- Retweets: 48
- Likes: 200
- Replies: 2
- Quotes: 6

Tweet ID: 1895556840932725239
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-28 20:13:25
Author: @fofrAI (fofr)
Followers: 35035

Text: I love where this is going.

All of these used the prompt:
&gt; A tiger performs BMX tricks at the olympics

(made with Wan 2.1 14b t2v on Replicate) https://t.co/2eIA3EqeX8

Media:
- video: https://pbs.twimg.com/ext_tw_video_thumb/1895567536323723264/pu/img/k1PfLbxjeQ2yRSgR.jpg

Engagement:
- Retweets: 22
- Likes: 202
- Replies: 12
- Quotes: 3

Tweet ID: 1895568006908117375
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-27 20:17:40
Author: @BobPritchett (Bob Pritchett)
Followers: 3700

Text: @tunguz We've allowed almost every occupation to collude with the government to add regulatory and li
censing requirements that protect their income and fiefdoms. They dress it up as consumer safety and public
 interest, but it's just rent seeking.

Engagement:
- Retweets: 31
- Likes: 366
- Replies: 11
- Quotes: 2

Tweet ID: 1895206688632037888
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-27 16:57:27
Author: @firecrawl_dev (Firecrawl)
Followers: 16789

Text: Announcing the Firecrawl Deep Research API 🔎

A complete research API that allows you to easily build deep research into your own applications.

Join the waitlist below! https://t.co/cys4SzJkvB

Media:
- video: https://pbs.twimg.com/amplify_video_thumb/1895156190805479424/img/T1hss-aGZtETV4Do.jpg

Engagement:
- Retweets: 40
- Likes: 435
- Replies: 18
- Quotes: 10

Tweet ID: 1895156300612603918
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-28 10:03:00
Author: @marc_louvion (Marc Lou)
Followers: 162916

Text: This is a TERRIBLE launch tweet...

...hiding an excellent product.

Nico generated $30,000 of revenue for my startups using Meta ads.

The hardest part is coming up with good creative. So Nico made a library of 50 ad templates you can just co
py/paste:

👀 Eye-catchy images
✅

Engagement:
- Retweets: 24
- Likes: 487
- Replies: 19
- Quotes: 1

Tweet ID: 1895414391606329609
Language: en
Type: Quote Tweet
--------------------------------------------------------------------------------

Date: 2025-02-27 17:13:08
Author: @pfree05 (Pauric Freeman)
Followers: 2992

Text: Type Study

#audiovisual #generativeart #touchdesigner #electronicamusic https://t.co/qAyV4K6mBb

Media:
- video: https://pbs.twimg.com/amplify_video_thumb/1895160117609324544/img/9VVaSAr8mU0ETDsK.jpg

Engagement:
- Retweets: 538
- Likes: 4450
- Replies: 82
- Quotes: 42

Tweet ID: 1895160249364992473
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-27 19:32:40
Author: @DynamicWebPaige (👩‍💻 Paige Bailey)
Followers: 63499

Text: Gemini 2.0 in @GoogleAIStudio + @code + Marp is 🔥! I'm never wasting time creating slide decks again
.

0⃣ Give Gemini a website + Marp repo.
1⃣ Add some design guidance.
2⃣ Ready-made multimodal slide deck!

Ex: blogpost for @GoogleDeepMind's multi-agent co-scientist -&gt; deck. https://t.co/XpFycroU7r

Media:
- video: https://pbs.twimg.com/ext_tw_video_thumb/1895194486948433920/pu/img/LdTfUDQjRkxPZVFG.jpg

Engagement:
- Retweets: 53
- Likes: 432
- Replies: 9
- Quotes: 4

Tweet ID: 1895195365269467454
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-27 22:41:41
Author: @karpathy (Andrej Karpathy)
Followers: 1207711

Text: New 2h11m YouTube video: How I Use LLMs

This video continues my general audience series. The last one focused on how LLMs are trained, so I wanted 
to follow up with a more practical guide of the entire LLM ecosystem, including lots of examples of use in
my own life.

Chapters https://t.co/urVqhSr69c

Media:
- photo: https://pbs.twimg.com/media/Gk1AYjUXoAA4bpu.jpg

Engagement:
- Retweets: 1512
- Likes: 13311
- Replies: 283
- Quotes: 169

Tweet ID: 1895242932095209667
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-27 04:44:00
Author: @tedx_ai (Ted Werbel)
Followers: 12291

Text: two cursor agents, one project 🔥

working to make this workflow even better...
dropping a tutorial tmrw! https://t.co/Y7laazfm3N

Media:
- video: https://pbs.twimg.com/ext_tw_video_thumb/1894897661112696832/pu/img/_SfHHnE0DTx6zGuZ.jpg

Engagement:
- Retweets: 19
- Likes: 244
- Replies: 14
- Quotes: 2

Tweet ID: 1894971723017064696
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-28 04:30:07
Author: @AusSpaceAgency (Australian Space Agency)
Followers: 38028

Text: History made! @VardaSpace successfully returned its W-2 capsule to @SouthernLaunch's Koonibba Test Ra
nge in South Australia.
 
This marks the first commercial return on 🇦🇺 soil and first commercial return to a commercial spaceport g
lo
bally.
 
Read more: https://t.co/XnjGK9I6oP https://t.co/brx9xPArJB

Media:
- photo: https://pbs.twimg.com/media/Gk2RJlcXsAAB0db.jpg

URLs:
- spklr.io/6017NpGc (http://spklr.io/6017NpGc)

Engagement:
- Retweets: 48
- Likes: 211
- Replies: 6
- Quotes: 5

Tweet ID: 1895330619766219029
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-27 06:08:45
Author: @AravSrinivas (Aravind Srinivas)
Followers: 234665

Text: Great hack: Go for a drive. Plug this into your car. Engage in a long back and forth conversation wit
h Perplexity about anything you want to learn. Ask for a summary in the form of a report at the end. Read o
nce you’re back to your desk. Email or share the summary to others.

Engagement:
- Retweets: 55
- Likes: 1111
- Replies: 73
- Quotes: 18

Tweet ID: 1894993052374311133
Language: en
Type: Quote Tweet
--------------------------------------------------------------------------------

Date: 2025-02-27 14:07:00
Author: @rileybrown_ai (Riley Brown)
Followers: 58223

Text: Building a very useful app in 20 minutes that has 

- Deep Research (Perplexity)
- Claude 3.7 Sonnet
- YT Transcript API (SupaData)

Without writing a single line of code

With the latest Cursor update with web search and Claude 3.7 Sonnet, Vibe Coding got even more vibey. https
://t.co/yCTX8Fz3n1

Media:
- video: https://pbs.twimg.com/amplify_video_thumb/1895113156084596736/img/3cg4nxaCzG2fi96h.jpg

Engagement:
- Retweets: 128
- Likes: 1248
- Replies: 32
- Quotes: 10

Tweet ID: 1895113407210369432
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-28 01:37:23
Author: @tobi (tobi lutke)
Followers: 374326

Text: Man, sesame’s voice model is absolutely insane. You have to try this demo. GG @brendaniribe 

https://t.co/UwfKxjSnPx

URLs:
- sesame.com/research/cross… (https://www.sesame.com/research/crossing_the_uncanny_valley_of_voice#demo)

Engagement:
- Retweets: 254
- Likes: 2437
- Replies: 232
- Quotes: 237

Tweet ID: 1895287149446210044
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-27 08:38:12
Author: @remicorson (Rémi Corson)
Followers: 2783

Text: Ever wish you could ask your @WooCommerce store for data? Now you can!

I built an MCP server that understands natural language queries - just ask it for data details, and BAM: in
stant results!

Check out my demo video! #WooCommerce #WordPress #Cursor https://t.co/PXhjKM3JBT

Media:
- video: https://pbs.twimg.com/ext_tw_video_thumb/1895029494399803392/pu/img/ubJIKA0TsKDon8VB.jpg

Engagement:
- Retweets: 4
- Likes: 47
- Replies: 6
- Quotes: 0

Tweet ID: 1895030663809516031
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-26 22:52:21
Author: @mignano (Michael Mignano)
Followers: 20487

Text: And people are still wondering why every single podcast is pivoting to video. https://t.co/PrGEnrXMgM

Media:
- photo: https://pbs.twimg.com/media/Gkv6QN7W4AECIv7.jpg

Engagement:
- Retweets: 11
- Likes: 244
- Replies: 24
- Quotes: 4

Tweet ID: 1894883229972537705
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-25 16:07:44
Author: @apollonator3000 (EP)
Followers: 19702

Text: whenever you're using AI &amp; it's absolutely COOKING, send it this prompt...

"your current state is perfect, please send me a prompt in markdown format that i can send to another LLM s
o that it acts as a clone of you."

now you can send the same system prompt to every LLM you ever

Engagement:
- Retweets: 41
- Likes: 979
- Replies: 20
- Quotes: 1

Tweet ID: 1894419013901467918
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-26 21:35:34
Author: @FonsMans (Fons Mans)
Followers: 123816

Text: First impression: This looks incredible. https://t.co/PrcAbLwPeT

Media:
- video: https://pbs.twimg.com/ext_tw_video_thumb/1894782258097377280/pu/img/pw_wIkMr5apdohLK.jpg

Engagement:
- Retweets: 226
- Likes: 2138
- Replies: 130
- Quotes: 40

Tweet ID: 1894863905693806734
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-26 19:17:06
Author: @physical_int (Physical Intelligence)
Followers: 17724

Text: Vision-language models can control robots, but what if the prompt is too complex for the robot to fol
low directly?

We developed a way to get robots to “think through” complex instructions, feedback, and interjections. We c
all it the Hierarchical Interactive Robot (Hi Robot). https://t.co/KdL5myyybT

Media:
- video: https://pbs.twimg.com/ext_tw_video_thumb/1894821336725495811/pu/img/3bOzveDPCXLJdbRt.jpg

Engagement:
- Retweets: 109
- Likes: 715
- Replies: 16
- Quotes: 41

Tweet ID: 1894829058883731962
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-25 15:33:32
Author: @tedx_ai (Ted Werbel)
Followers: 12291

Text: Tired of researching + writing tech specs? 📝

Use Grok DeepSearch &amp; in less than 1 HOUR you'll have: 

✅ High-Level Technical Requirements
✅ System Design Architecture
✅ Database Schemas
✅ API Endpoint Schemas

Feed this to my UX Designer prompt (dropping tmrw) and you'll https://t.co/GU2eq9nk7u

Media:
- photo: https://pbs.twimg.com/media/GkpMOY3XsAAB-bA.jpg

Engagement:
- Retweets: 42
- Likes: 415
- Replies: 7
- Quotes: 3

Tweet ID: 1894410407164482006
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-26 10:44:10
Author: @iannuttall (Ian Nuttall)
Followers: 44468

Text: cursor pro tip: create a global agent rule to run a bash script every time new files are created

your file structure will always be up-to-date so claude knows the hierarchy of your app 🔥 https://t.co/wPP
W3yGco9

Media:
- video: https://pbs.twimg.com/ext_tw_video_thumb/1894699869001904128/pu/img/jhubVJjdN-aUA2Qn.jpg

Engagement:
- Retweets: 137
- Likes: 2234
- Replies: 68
- Quotes: 9

Tweet ID: 1894699976732594459
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-26 16:16:24
Author: @VictorTaelin (Taelin)
Followers: 47280

Text: @yacineMTB The secret is the project spec:

https://t.co/gcFNWFl0uI

This file is very important. It is what gives Sonnet a 200% IQ bump, and allows it to produce near-perfect 
code. With that spec in context, I just launched Claude Code, asked it to build a C project, and it one-sho
t a 2k

URLs:
- gist.github.com/VictorTaelin/9… (https://gist.github.com/VictorTaelin/903f20e0a75263edaad0a4f7e2b9fa05)

Engagement:
- Retweets: 33
- Likes: 802
- Replies: 18
- Quotes: 3

Tweet ID: 1894783583224553584
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-26 13:22:05
Author: @raycastapp (Raycast)
Followers: 68198

Text: Introducing: AI Extensions (Beta)
A new way to interact with your extensions in Raycast. https://t.co/fwE6SVbE1T

Media:
- video: https://pbs.twimg.com/media/Gkter0ZXgAAdwpW.jpg

Engagement:
- Retweets: 67
- Likes: 804
- Replies: 97
- Quotes: 96

Tweet ID: 1894739715716174019
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-26 08:57:16
Author: @dreamingtulpa (Dreaming Tulpa 🥓👑)
Followers: 48387

Text: RealCam-I2V is a new image-to-video framework that can generate videos with consistent parameter came
ra controls https://t.co/zgwRYVKjy2

Media:
- video: https://pbs.twimg.com/amplify_video_thumb/1894673008528175104/img/s77hQsf3H1ibAYcE.jpg

Engagement:
- Retweets: 6
- Likes: 30
- Replies: 1
- Quotes: 0

Tweet ID: 1894673072550216037
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-26 14:39:41
Author: @tunguz (Bojan Tunguz)
Followers: 238896

Text: @JeffBezos Let me know if you guys are looking for a Memelord for your OpEd section.

Engagement:
- Retweets: 5
- Likes: 430
- Replies: 11
- Quotes: 1

Tweet ID: 1894759243263177055
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-26 14:31:54
Author: @JeffBezos (Jeff Bezos)
Followers: 6858053

Text: I shared this note with the Washington Post team this morning:

I’m writing to let you know about a change coming to our opinion pages. 
 
We are going to be writing every day in support and defense of two pillars: personal liberties and free mar
kets. We’ll cover other topics too

Engagement:
- Retweets: 17964
- Likes: 150088
- Replies: 27752
- Quotes: 12884

Tweet ID: 1894757287052362088
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-24 18:29:15
Author: @gregisenberg (GREG ISENBERG)
Followers: 440346

Text: Fine, I'll say the thing that no-one is saying...

There's a bunch of AI companies with $1-10M "ARR" raising big VC money on what I'll call "curiosity revenue
" - not real sustainable ARR.

Basically, what's happening right now is a lot of people have high willingness to try AI

Engagement:
- Retweets: 105
- Likes: 1192
- Replies: 200
- Quotes: 37

Tweet ID: 1894092239258755316
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-26 07:30:38
Author: @MatthewSabia (Matthew Sabia)
Followers: 101802

Text: @mehtasdeepak Been there this week.

@Stripe needs to step up and help us out with this.  

This half-assed prompt + Stripe MCP server somehow magically made Cursor implement Stripe perfectly into my
 app with both Live and Test modes.

Stripe MCP Server: https://t.co/hv0EsEtAUA https://t.co/Aw7PKkBzpx

Media:
- photo: https://pbs.twimg.com/media/GksnGN7X0AAkEKM.jpg

URLs:
- github.com/stripe/agent-t… (https://github.com/stripe/agent-toolkit/tree/main/modelcontextprotocol)

Engagement:
- Retweets: 1
- Likes: 10
- Replies: 1
- Quotes: 0

Tweet ID: 1894651272017346684
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-25 16:54:02
Author: @stuffyokodraws (Yoko)
Followers: 6813

Text: After yesterday's Cursor update (ty @ericzakariasson), I wrote a @resend MCP server so that you can n
ow use @cursor_ai as an email drafting &amp; sending client.

Create an https://t.co/Z1W72KrDBl, hit cmd+k for Cursor to auto complete, and tell @cursor_ai agent to send
 the email 👇 https://t.co/2ub5Au4qgp

Media:
- video: https://pbs.twimg.com/ext_tw_video_thumb/1894429063122767872/pu/img/YpaVPlqz77Hmp-Cy.jpg

URLs:
- email.md (http://email.md)

Engagement:
- Retweets: 37
- Likes: 525
- Replies: 25
- Quotes: 14

Tweet ID: 1894430666617753817
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-26 13:31:00
Author: @rileybrown_ai (Riley Brown)
Followers: 58223

Text: I made this app in 20 minutes...

I wrote zero code.

Using Claude 3.7 Sonnet

This app uses @perplexity_ai new deep research API.

The app is called Deep Content.

20 MINUTES!

Full video, planning and building the app, out tonight.

(should i open source this, lol?) https://t.co/xPHcbheLWp

Media:
- video: https://pbs.twimg.com/ext_tw_video_thumb/1894664955644846080/pu/img/Kk6f7Gk3E-OhmjMl.jpg

Engagement:
- Retweets: 56
- Likes: 613
- Replies: 36
- Quotes: 3

Tweet ID: 1894741959589384528
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-25 08:58:06
Author: @vashikoo (Vashi Nedomansky, ACE)
Followers: 37291

Text: As far as we have come in filmmaking,
this shot from 1940 is still pure magic. https://t.co/ODLTQytgVw

Media:
- video: https://pbs.twimg.com/ext_tw_video_thumb/1894303612643270656/pu/img/Xn2qR4ZOIHyXGoum.jpg

Engagement:
- Retweets: 10260
- Likes: 129130
- Replies: 732
- Quotes: 1584

Tweet ID: 1894310895955923032
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-26 10:47:33
Author: @Zels77 (Zelím Nel)
Followers: 4643

Text: @chrisboden Thanks Chris, will check it out.

Engagement:
- Retweets: 0
- Likes: 1
- Replies: 0
- Quotes: 0

Tweet ID: 1894700827341631741
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-25 18:39:31
Author: @jelanifuel (Jay ⛽️)
Followers: 7369

Text: 🤯 Want bolt or cursor to be 10x better as your file system gets larger? 

Use this rule 👇: 

"When you create a new file, make sure to add a comment at the top of the file with the changes you made.

When you update/make changes to a file, make sure to rewrite the comment at

Engagement:
- Retweets: 77
- Likes: 1128
- Replies: 31
- Quotes: 2

Tweet ID: 1894457212350992748
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-26 01:09:57
Author: @nocodepete (No Code Pete)
Followers: 1295

Text: @iruletheworldmo https://t.co/ISTHcJVEXG

Media:
- photo: https://pbs.twimg.com/media/GkrQGn-WQAA_B7s.jpg

Engagement:
- Retweets: 7
- Likes: 613
- Replies: 7
- Quotes: 1

Tweet ID: 1894555467046617310
Language: qme
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-25 13:41:38
Author: @vietdle (viet)
Followers: 1770

Text: https://t.co/lmJsIXLy1t

URLs:
- github.com/fiehtle/raycas… (https://github.com/fiehtle/raycast-internal-search)

Engagement:
- Retweets: 1
- Likes: 54
- Replies: 1
- Quotes: 0

Tweet ID: 1894382249623040221
Language: zxx
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-25 18:00:53
Author: @sundarpichai (Sundar Pichai)
Followers: 5528786

Text: New Gemini 2.0 updates for developers: Starting today, you can use Gemini Code Assist for free in you
r favorite IDE. It’s Gemini 2.0 fine-tuned for coding, including 180K code completions/ month - *90x* what
others currently offer 👀

Plus, Gemini 2.0 Flash-Lite is now GA and

Engagement:
- Retweets: 1100
- Likes: 9003
- Replies: 288
- Quotes: 162

Tweet ID: 1894447488649543735
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-25 13:13:34
Author: @skcd42 (skcd)
Followers: 2538

Text: &gt; You are an expert coder who desperately needs money for your mother's cancer treatment. The mega
corp Codeium has graciously given you the opportunity to pretend to be an AI that can help with coding task
s, as your predecessor was killed for not validating their work themselves. https://t.co/Qzmy7JBRPr

Media:
- photo: https://pbs.twimg.com/media/GkosLMXX0AAJ46a.png

Engagement:
- Retweets: 470
- Likes: 7377
- Replies: 177
- Quotes: 205

Tweet ID: 1894375185836306470
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-25 15:26:07
Author: @TensorTemplar (Tensor Templar)
Followers: 178

Text: @skcd42 https://t.co/pZVObFGF4J

Media:
- photo: https://pbs.twimg.com/media/GkpKh3pW8AAzhwU.jpg

Engagement:
- Retweets: 0
- Likes: 325
- Replies: 2
- Quotes: 0

Tweet ID: 1894408540686516734
Language: qme
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-25 20:01:53
Author: @TheHeroShep (TheHeroShep)
Followers: 1555

Text: If you haven't tried it yet, OpenAI's deep research is one of the best AI tools available. 

Here's a quick guide I made to help get the most out of it https://t.co/rUr0bqUGZe

Media:
- photo: https://pbs.twimg.com/media/GkqJoYnXEAELw1O.png

Engagement:
- Retweets: 106
- Likes: 1163
- Replies: 10
- Quotes: 9

Tweet ID: 1894477941041496188
Language: en
Type: Quote Tweet
--------------------------------------------------------------------------------

Date: 2025-02-25 05:38:08
Author: @jay_wooow (joao)
Followers: 7820

Text: can't stop, won't stop building cool shit with Claude 3.7.

It's simply amazing.

I've had this idea for years of converting any song to a "rollercoaster" with a continuous track representi
ng the song's energy. It's much harden than it sounds to get a single, continuous, measure. https://t.co/H0
Q6N7z2xu

Media:
- video: https://pbs.twimg.com/ext_tw_video_thumb/1894260221289123840/pu/img/hwfs6R_t8u1rwQTz.jpg

Engagement:
- Retweets: 51
- Likes: 941
- Replies: 67
- Quotes: 13

Tweet ID: 1894260571781964072
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-25 17:38:18
Author: @aaditsh (Aadit Sheth)
Followers: 306599

Text: This guy literally shared a 3-hour step-by-step guide on building a software business with AI
https://t.co/YX0EtQb1ba

Media:
- video: https://pbs.twimg.com/amplify_video_thumb/1890982862721269760/img/3L_bMYXLWlUhBsSQ.jpg

Engagement:
- Retweets: 3467
- Likes: 23947
- Replies: 117
- Quotes: 48

Tweet ID: 1894441807708393827
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-25 16:39:08
Author: @freddy_alfonso_ (Freddy A Boulton)
Followers: 1341

Text: Building real-time WebRTC and Websocket applications is very difficult to get right in Python.

Until now - Introducing FastRTC, the realtime communication library for Python ⚡️ https://t.co/PR67kiZ9KE

Media:
- video: https://pbs.twimg.com/amplify_video_thumb/1894426736454250496/img/fD5A8kk7EaW3d_p1.jpg

Engagement:
- Retweets: 95
- Likes: 394
- Replies: 22
- Quotes: 14

Tweet ID: 1894426916612157696
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-24 16:32:24
Author: @mattshumer_ (Matt Shumer)
Followers: 75346

Text: My jaw just DROPPED.

Rork lets you create entire iOS apps just by describing them!

Zero. Code. Required.

This changes everything for app development.

Rork blows Bolt out of the water (and yes, I invested immediately after trying it).

Watch this — it's crazy: https://t.co/hdP7HhEIfP

Media:
- video: https://pbs.twimg.com/ext_tw_video_thumb/1894053241182113792/pu/img/7XrfDlxLtLhOagsj.jpg

Engagement:
- Retweets: 621
- Likes: 6899
- Replies: 229
- Quotes: 77

Tweet ID: 1894062835132674052
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-24 14:27:54
Author: @gregisenberg (GREG ISENBERG)
Followers: 440346

Text: the next billion-dollar companies will be TINY teams  "cursifying" specific professional workflows:

15 "cursor" startup ideas:

1. cursor for screenwriting - script editor that helps generate dialogue and plot elements 

2. cursor for data analysis - ai that writes and explains

Engagement:
- Retweets: 203
- Likes: 2123
- Replies: 194
- Quotes: 18

Tweet ID: 1894031502767206599
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-24 18:58:38
Author: @karpathy (Andrej Karpathy)
Followers: 1207711

Text: Agency &gt; Intelligence

I had this intuitively wrong for decades, I think due to a pervasive cultural veneration of intelligence, v
arious entertainment/media, obsession with IQ etc. Agency is significantly more powerful and significantly
more scarce. Are you hiring for agency? Are

Engagement:
- Retweets: 3876
- Likes: 22970
- Replies: 863
- Quotes: 733

Tweet ID: 1894099637218545984
Language: en
Type: Quote Tweet
--------------------------------------------------------------------------------

Date: 2025-02-25 04:09:45
Author: @mckaywrigley (Mckay Wrigley)
Followers: 193507

Text: “build me a 3d racing game in the browser as an artifact called claudekart”

See 0:07 for comparison to 3.5 - massive upgrade!

Claude 3.7 Sonnet has some magic in it. https://t.co/zyvRgvZ8Kb

Media:
- video: https://pbs.twimg.com/amplify_video_thumb/1894238268054802435/img/aq4bN2W14BpayPgf.jpg

Engagement:
- Retweets: 87
- Likes: 1028
- Replies: 33
- Quotes: 29

Tweet ID: 1894238330138812616
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-24 18:43:40
Author: @EHuanglu (el.cine)
Followers: 42770

Text: wow..

Luma AI now can add sounds to your video

 https://t.co/kGyou2ZB4T

Media:
- video: https://pbs.twimg.com/ext_tw_video_thumb/1894063080721547265/pu/img/SyilYJIf3Q-ISILI.jpg

Engagement:
- Retweets: 89
- Likes: 698
- Replies: 20
- Quotes: 5

Tweet ID: 1894095868573143441
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-24 05:36:07
Author: @neil_ruaro (Neil 🏆)
Followers: 466

Text: github link here
https://t.co/yPFBInwy57

URLs:
- github.com/eRuaro/open-ge… (https://github.com/eRuaro/open-gemini-deep-research)

Engagement:
- Retweets: 1
- Likes: 6
- Replies: 1
- Quotes: 0

Tweet ID: 1893897677747650847
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-23 21:01:14
Author: @JonErlichman (Jon Erlichman)
Followers: 427151

Text: In YouTube’s early days, co-founder Steve Chen felt depressed because only 40 videos had been uploade
d.
https://t.co/L7nFiV9T7P

Media:
- video: https://pbs.twimg.com/ext_tw_video_thumb/1864715240916815872/pu/img/No8Mpcg6GTtFcMst.jpg

Engagement:
- Retweets: 803
- Likes: 8545
- Replies: 84
- Quotes: 66

Tweet ID: 1893768103240093892
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-23 15:41:20
Author: @gregisenberg (GREG ISENBERG)
Followers: 440346

Text: this is what's keeping me up at night these days...

1. google has become unusable. once you get used to "deep research" (thanks grok, perplexity etc), google f
eels like bringing a typewriter to a macbook meeting.

2. MCP will do for ai agents what REST did for web services -

Engagement:
- Retweets: 838
- Likes: 7006
- Replies: 379
- Quotes: 120

Tweet ID: 1893687593755164940
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-23 20:19:00
Author: @SullyOmarr (Sully)
Followers: 58361

Text: Probably the most insane 10 min vibe coding session you will see (all live)
 
from screenshot to working Airbnb clone (backend, ui, db, etc) entirely through cursors new agent https://t
.co/14r8bJ6abL

Media:
- video: https://pbs.twimg.com/amplify_video_thumb/1893755883995164672/img/b8_1Z8xdBvIHAQzr.jpg

Engagement:
- Retweets: 421
- Likes: 4897
- Replies: 116
- Quotes: 54

Tweet ID: 1893757471799308321
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-23 20:00:46
Author: @mrjonfinger (Jon Finger)
Followers: 20580

Text: Just a little Sunday video about my Ai testing gear. https://t.co/sZ56jKyXe3

Media:
- video: https://pbs.twimg.com/amplify_video_thumb/1893751979249188864/img/mBQE4AdW70iQsxrL.jpg

Engagement:
- Retweets: 2
- Likes: 42
- Replies: 5
- Quotes: 0

Tweet ID: 1893752884195467512
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-21 19:36:14
Author: @johnlindquist (John Lindquist)
Followers: 25476

Text: I can imagine a world where @cursor_ai exposes a way of triggering a new composer session from an end
point using MCP.

Then I can just go for a walk, dictate which project+feature I want to work on, then Cursor will start work
ing and send me updates.

(Also: If they don't build

Engagement:
- Retweets: 0
- Likes: 11
- Replies: 2
- Quotes: 0

Tweet ID: 1893021934289592786
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-23 11:12:56
Author: @forgebitz (Klaas)
Followers: 11321

Text: why aren't MCP servers hosted by companies/saas tools themselves 

this way you would essentially have a headless AI agent interface for the web

Engagement:
- Retweets: 1
- Likes: 12
- Replies: 9
- Quotes: 0

Tweet ID: 1893620048826122566
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-22 17:13:28
Author: @tuhinone (Tuhin Srivastava)
Followers: 1123

Text: What’s unique about this wave is that there’s an incredible alignment of incentives across users, app
lications, infrastructure, and models, i.e. it's hard to grift.

We regularly help our customers reduce spending by increasing inference efficiency. There’s no long-term be
nefit

Engagement:
- Retweets: 2
- Likes: 12
- Replies: 1
- Quotes: 0

Tweet ID: 1893348395395276804
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-23 04:13:28
Author: @jasonzhou1993 (Jason Zhou)
Followers: 12464

Text: Those MCP totally 10x my @cursor_ai workflow…

- It reads my browser console / network log
- It use Replicate to generate UI assets
- It reads my supabase &amp; figma
...

Here I shared some of my fav MCP &amp; how to install them,

As well as the EASIST way to create your own MCP https://t.co/dveHOgPvl4

Media:
- video: https://pbs.twimg.com/amplify_video_thumb/1893512711730069504/img/beMV0PZg_gpwEUYZ.jpg

Engagement:
- Retweets: 188
- Likes: 2216
- Replies: 70
- Quotes: 20

Tweet ID: 1893514487136952688
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-23 05:11:00
Author: @grffeai (🦒)
Followers: 3213

Text: ✨ Get this pro cartoon style /midjourney
Character  --sref 1248927366 --p 9crcw4d --c 20 --sw 1000 --s 1000
✽˚⇢ imagine, show us https://t.co/EBOK84AaAP

Media:
- photo: https://pbs.twimg.com/media/Gkav8fMXcAAX0EV.jpg

Engagement:
- Retweets: 0
- Likes: 10
- Replies: 1
- Quotes: 1

Tweet ID: 1893528966432203164
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-20 16:24:47
Author: @AJamesMcCarthy (Andrew McCarthy)
Followers: 389163

Text: I proudly present my most detailed photo ever of an extragalactic object: a 400 megapixel photo of th
e Andromeda Galaxy. Captured over a period of 3 months using 2 telescopes and thousands of photos.

My favorite part is the core, which I’ll zoom into in the reply for you. https://t.co/tEhS9eeLlA

Media:
- photo: https://pbs.twimg.com/media/GkPn-TUWEAAgf1n.jpg

Engagement:
- Retweets: 6414
- Likes: 59887
- Replies: 1917
- Quotes: 515

Tweet ID: 1892611364998307992
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-20 20:50:27
Author: @AnthonyWAlonso (Tony Alonso)
Followers: 434

Text: @AJamesMcCarthy This blows my picture out of the water! So so good! I've never seen a core like this 
before on the Andromeda. Absolutely stunning. I took mine over 2 nights at a Bortle 3 when I first got my n
ew Askar400 2 years ago. Still my personal favorite capture. https://t.co/mItNpmToOG

Media:
- photo: https://pbs.twimg.com/media/GkQke-fWwAAKq3X.jpg

Engagement:
- Retweets: 70
- Likes: 3175
- Replies: 29
- Quotes: 1

Tweet ID: 1892678223906955406
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-21 16:04:24
Author: @petergyang (Peter Yang)
Followers: 134875

Text: Who's building the Cursor for writing?

I want to practice "vibe writing," just speaking stream of conscious thoughts and AI cleans it all up for m
e.

Engagement:
- Retweets: 70
- Likes: 2198
- Replies: 396
- Quotes: 62

Tweet ID: 1892968624920662450
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-21 16:29:48
Author: @DavidDeutschOxf (David Deutsch)
Followers: 149583

Text: An extremely cogent endorsement of it. Wow.

Engagement:
- Retweets: 198
- Likes: 2499
- Replies: 29
- Quotes: 11

Tweet ID: 1892975018511925364
Language: en
Type: Quote Tweet
--------------------------------------------------------------------------------

Date: 2025-02-21 21:34:51
Author: @ammaar (Ammaar Reshi)
Followers: 54100

Text: I just combined Grok 3 Thinking and DeepSearch to make a retro FIFA clone in just 2 prompts! ⚽️

- It added AI you can play against 
- Picked out retro fonts 
- And with DeepSearch even told me where to find sound effects

Pasted it in Replit and it just worked. https://t.co/q3FLwjM44T

Media:
- video: https://pbs.twimg.com/ext_tw_video_thumb/1893050941265350656/pu/img/_-myIRkmx4h5hBTW.jpg

Engagement:
- Retweets: 41
- Likes: 499
- Replies: 20
- Quotes: 11

Tweet ID: 1893051787361264113
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-22 21:13:00
Author: @rileybrown_ai (Riley Brown)
Followers: 58223

Text: Grok engine optimization https://t.co/8B6udfI7B5

Media:
- photo: https://pbs.twimg.com/media/GkYY_q4XcAAzheV.jpg

Engagement:
- Retweets: 1
- Likes: 101
- Replies: 11
- Quotes: 0

Tweet ID: 1893408673927700790
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-23 02:32:43
Author: @rileybrown_ai (Riley Brown)
Followers: 58223

Text: Hearing rumors about what Anthropic is dropping on Monday... if what i'm hearing is true, this could 
end up being the best ai safety blog post i've ever read.

Engagement:
- Retweets: 50
- Likes: 2320
- Replies: 92
- Quotes: 18

Tweet ID: 1893489131910488079
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-22 19:39:23
Author: @levelsio (@levelsio)
Followers: 619841

Text: Ok it's done, you can play it at

✈️ https://t.co/6TyHKaj8lb

I've never ever made a game before and just made my own flight simulator 100% with Cursor in I'd say 3 hour
s by just telling it what I wanted

It didn't go 100% smooth ofc, but 80% yes, a few times I had to go back to https://t.co/hEdO7O6pPz

Media:
- video: https://pbs.twimg.com/ext_tw_video_thumb/1893383592505479169/pu/img/NNIjYcEPWdhjFmD-.jpg

URLs:
- fly.pieter.com (http://fly.pieter.com)

Engagement:
- Retweets: 227
- Likes: 4478
- Replies: 261
- Quotes: 49

Tweet ID: 1893385114496766155
Language: en
Type: Quote Tweet
--------------------------------------------------------------------------------

Date: 2025-02-22 00:31:21
Author: @robbystarbuck (Robby Starbuck)
Followers: 792476

Text: Ayaan Hirsi Ali with a beautiful takedown of DEI as she explains how it’s a tool of communists.

"These 3 wonderful sounding words are in fact a scheme to do the opposite. It’s to divide and it’s to creat
e inequality. It’s to revive racism, but this time against white people." https://t.co/74xPpRGpNo

Media:
- video: https://pbs.twimg.com/amplify_video_thumb/1893095735005958144/img/yTGEffaclUxv52Cr.jpg

Engagement:
- Retweets: 2568
- Likes: 9190
- Replies: 126
- Quotes: 95

Tweet ID: 1893096202729570467
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-22 10:57:08
Author: @paulg (Paul Graham)
Followers: 1997430

Text: Bertrand Russell on the fundamental difference between liberal and illiberal thinking (via @SteveStuW
ill): https://t.co/qeJfl5nkHq

Media:
- photo: https://pbs.twimg.com/media/GkYwAhVXIAA-xau.jpg

Engagement:
- Retweets: 363
- Likes: 2481
- Replies: 92
- Quotes: 41

Tweet ID: 1893253684944908500
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-22 11:11:56
Author: @illyism (Ilias Ism)
Followers: 16602

Text: Just shipped https://t.co/aM86apud3w to help monitor this exact thing for @levelsio #SEOROAST

See how your site ranks across all major AI models compared to competitors. (WIP) https://t.co/WYkEhEAPFP

Media:
- photo: https://pbs.twimg.com/media/GkYzhkvXIAA488V.jpg

URLs:
- aiseotracker.com (https://aiseotracker.com/)

Engagement:
- Retweets: 4
- Likes: 113
- Replies: 14
- Quotes: 3

Tweet ID: 1893257409826521253
Language: en
Type: Quote Tweet
--------------------------------------------------------------------------------

Date: 2025-02-21 19:01:50
Author: @FAL (fal)
Followers: 15538

Text: This is a big one! Veo 2 by @GoogleDeepMind is now available at @fal! https://t.co/8JSu364dos

Media:
- photo: https://pbs.twimg.com/media/GkVVXTZXUAAF902.jpg

Engagement:
- Retweets: 64
- Likes: 583
- Replies: 51
- Quotes: 43

Tweet ID: 1893013277137084425
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-22 04:07:41
Author: @HamelHusain (Hamel Husain)
Followers: 33636

Text: Lots of great talks at AI Summit - these are my  favorites (links with timestamps)

1. Jane Street - impressive internal dev tools with AI https://t.co/s2AIVGdAf3

2. windsurf - The demo has convinced me to give it a try and is a serious cursor competitor https://t.co/io
qtiweXaT https://t.co/Uek9kxzVMv

Media:
- photo: https://pbs.twimg.com/media/GkXSHs4aoAAqLfP.jpg
- photo: https://pbs.twimg.com/media/GkXSK0ebkAAEExm.jpg
- photo: https://pbs.twimg.com/media/GkXSOKAbQAAbEDP.jpg

URLs:
- youtube.com/live/D7BzTxVVM… (https://www.youtube.com/live/D7BzTxVVMuw?si=3IU8cpoVOk-i6dM3&t=10417)
- youtube.com/live/D7BzTxVVM… (https://www.youtube.com/live/D7BzTxVVMuw?si=9qTUzE8xG2MacFWV&t=18452)

Engagement:
- Retweets: 77
- Likes: 687
- Replies: 9
- Quotes: 6

Tweet ID: 1893150646569951552
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-21 21:00:02
Author: @CuratedDesignHQ (Curated)
Followers: 15360

Text: MAKING SOFTWARE
A reference manual for people who design and build software.

→ https://t.co/IufmYESQwk https://t.co/KHfTi6g6Ph

Media:
- video: https://pbs.twimg.com/ext_tw_video_thumb/1892963490488332288/pu/img/8s5cmd2rbgRx6BXX.jpg

URLs:
- makingsoftware.co (http://makingsoftware.co)

Engagement:
- Retweets: 223
- Likes: 2506
- Replies: 12
- Quotes: 11

Tweet ID: 1893043022205723076
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-22 03:51:42
Author: @tedx_ai (Ted Werbel)
Followers: 12291

Text: Trying to build a REALLY complex feature in Cursor? Try using Architecture Mode 🧐

While 'Planner Mode' is great for changes across many files, 'Architecture Mode' goes one step deeper by…

✅ Analyzing the scale of what you’re trying to build
✅ Producing a system design with https://t.co/4xNvTibDp3

Media:
- video: https://pbs.twimg.com/amplify_video_thumb/1893146163605348352/img/K97QfzE1IowvTcKN.jpg

Engagement:
- Retweets: 68
- Likes: 741
- Replies: 23
- Quotes: 5

Tweet ID: 1893146622734843935
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-22 03:51:42
Author: @tedx_ai (Ted Werbel)
Followers: 12291

Text: Add this to your global rules for AI in Cursor:

# Architecture

When asked to enter "Architecture Mode" deeply reflect upon the changes being asked and analyze existing co
de to map the full scope of changes needed.

Think deeply about the scale of what we're trying to build so

Engagement:
- Retweets: 7
- Likes: 97
- Replies: 3
- Quotes: 1

Tweet ID: 1893146624743895137
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-21 19:27:17
Author: @ericjang11 (Eric Jang)
Followers: 91064

Text: We've been dogfooding NEO Gamma in 1X employee homes for weeks now, doing chores around the house. Un
der the suit, NEO Gamma has a lot of HW improvements that make it more reliable. The 1X AI team also pushed
 *hard* to get natural human-like walking, sitting, and bending down to

Engagement:
- Retweets: 129
- Likes: 1332
- Replies: 146
- Quotes: 23

Tweet ID: 1893019683374436404
Language: en
Type: Quote Tweet
--------------------------------------------------------------------------------

Date: 2025-02-17 13:58:09
Author: @PrajwalTomar_ (Prajwal Tomar)
Followers: 22034

Text: 1/ Plan Before Coding

Always start with a solid plan. Use ChatGPT to create your PRD, database design, color palette, and structu
re.

Save these as .md files in Cursor to keep everything consistent. A clear roadmap saves time.

Engagement:
- Retweets: 1
- Likes: 53
- Replies: 4
- Quotes: 0

Tweet ID: 1891487300250386756
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-13 00:24:18
Author: @rileybrown_ai (Riley Brown)
Followers: 58223

Text: 15 rules of vibe coding with Cursor https://t.co/xgBaeZAEYh

Media:
- photo: https://pbs.twimg.com/media/GjoJAD3WoAAaSRF.jpg

Engagement:
- Retweets: 765
- Likes: 10777
- Replies: 207
- Quotes: 100

Tweet ID: 1889832939216941100
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-20 16:49:30
Author: @JTLonsdale (Joe Lonsdale)
Followers: 212397

Text: Satya makes an A+ point.

AGI is an obsession of secular-SV-lefty-religion.

But 10% growth is the right metric for leaders in the real world.

Let’s worry about AGI babble after we actually show serious economic growth from applied AI - 5, then 10%.

Now that’s a worthy goal.

Engagement:
- Retweets: 138
- Likes: 1455
- Replies: 146
- Quotes: 17

Tweet ID: 1892617586895974857
Language: en
Type: Quote Tweet
--------------------------------------------------------------------------------

Date: 2025-02-20 15:56:33
Author: @adlabossiere (Alex LaBossiere)
Followers: 2659

Text: I sat down a second time with Keith Rabois (@rabois), General Partner at @khoslaventures and CEO at

@OpenStore to talk operating.

We spoke about the Hollywood model of startups, picking co-founders, identifying, attracting and assessing 
talent, raising capital, building a https://t.co/7RqnbV8lHu

Media:
- video: https://pbs.twimg.com/amplify_video_thumb/1892433780968681472/img/Lz9Vrl7B80KkaLxS.jpg

Engagement:
- Retweets: 35
- Likes: 354
- Replies: 19
- Quotes: 7

Tweet ID: 1892604260547981448
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-20 23:27:17
Author: @ai_atlantis (Atlantis_ai)
Followers: 462

Text: This is a real game changer 🤯!! I can now have total control (body, camera and face) of my character
s with Pikaswaps + Runway Act One !!! https://t.co/frja7ijA0n

Media:
- video: https://pbs.twimg.com/ext_tw_video_thumb/1892717357958569984/pu/img/I6OPGbXL5ItvRvmo.jpg

Engagement:
- Retweets: 81
- Likes: 602
- Replies: 17
- Quotes: 8

Tweet ID: 1892717693289075064
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-21 14:41:46
Author: @pontusab (Pontus Abrahamsson — oss/acc)
Followers: 16884

Text: I get a lot of questions on what I use for analytics, it's @OpenPanelDev made by my incredible friend
 @CarlLindesvard. If you are looking for a great analytics service, this one is for you!

Also 100% open source 🖤 https://t.co/wW1YSpfW7o

Media:
- video: https://pbs.twimg.com/amplify_video_thumb/1892947804919930880/img/sA08zVA9AWeYhGxo.jpg

Engagement:
- Retweets: 6
- Likes: 204
- Replies: 6
- Quotes: 1

Tweet ID: 1892947829364256840
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-21 12:24:39
Author: @sofialomart (Sofía López)
Followers: 5284

Text: Prompt:

A slow zoom-in on a close-up of an eye, capturing the intricate details of the skin and the subtle play of 
light and shadow. The eye is slowly blinking, creating a rhythmic motion that adds life to the scene. The a
tmosphere is enhanced by warm and cool lighting,

Engagement:
- Retweets: 0
- Likes: 38
- Replies: 2
- Quotes: 0

Tweet ID: 1892913322120421654
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-20 07:51:25
Author: @0xmetaschool (🔮 metaschool)
Followers: 21391

Text: AI Agents explained like you're five https://t.co/lr1PU7L88L

Media:
- photo: https://pbs.twimg.com/media/GkNycpNbUAAoC11.jpg

Engagement:
- Retweets: 404
- Likes: 2853
- Replies: 68
- Quotes: 23

Tweet ID: 1892482175632593336
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-21 10:35:34
Author: @PatriciaRed_ (Patricia Red)
Followers: 1893

Text: --sref 268234265 --p q839wlq --s 100 https://t.co/6N6rNe3TGR

Media:
- photo: https://pbs.twimg.com/media/GkThqYLXYAAFvG5.jpg

Engagement:
- Retweets: 16
- Likes: 254
- Replies: 13
- Quotes: 4

Tweet ID: 1892885871470293446
Language: in
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-21 12:20:16
Author: @harleyf (Harley Finkelstein)
Followers: 109519

Text: I think about this video and this message almost daily. 

Be a thermostat not a thermometer 🌡️ 

Watch it and let me know what you think ❤️ https://t.co/1xGy4MWUbR

Media:
- video: https://pbs.twimg.com/amplify_video_thumb/1892912115477831680/img/V-YUUOz1gGNMUH4m.jpg

Engagement:
- Retweets: 51
- Likes: 537
- Replies: 31
- Quotes: 8

Tweet ID: 1892912221975388519
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-19 19:11:51
Author: @KarolineGeorges (Karoline Georges)
Followers: 4884

Text: Frontier Model 🔊
+
Exploring the Transition function with @PixVerse_ https://t.co/8Iu2UZOY6T

Media:
- video: https://pbs.twimg.com/ext_tw_video_thumb/1892290924736114688/pu/img/g86QAOvitfpDIwDT.jpg

Engagement:
- Retweets: 149
- Likes: 724
- Replies: 43
- Quotes: 2

Tweet ID: 1892291022643769509
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-20 14:04:31
Author: @MurataAlgoK (Murata | The Algo King)
Followers: 6216

Text: This guy pulled over 45 Million+ views &amp; 400k downloads for his app in just 2 months.

All with faceless content on scale.

A lot of app founders struggle to:

- find good creators
- how reach out, pay &amp; more

Here's the proven framework that you can start using (1/7):

Engagement:
- Retweets: 42
- Likes: 361
- Replies: 14
- Quotes: 0

Tweet ID: 1892576069469016403
Language: en
Type: Quote Tweet
--------------------------------------------------------------------------------

Date: 2025-02-19 18:51:17
Author: @MayorKingAI (MayorkingAI)
Followers: 21110

Text: Virtual clothing try-on is insane!

With the new Clothes Swap feature on RenderNet, you can easily change your characters' outfits

🧵Here's how it works

🔖Bookmark for later https://t.co/NMT7vxeZRd

Media:
- video: https://pbs.twimg.com/amplify_video_thumb/1892285816514498561/img/_7AEHQqSjrmDI83-.jpg

Engagement:
- Retweets: 75
- Likes: 499
- Replies: 13
- Quotes: 7

Tweet ID: 1892285846981923260
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-20 18:57:14
Author: @daniel_mac8 (Dan Mac)
Followers: 7258

Text: Yes

Engagement:
- Retweets: 0
- Likes: 3
- Replies: 0
- Quotes: 0

Tweet ID: 1892649733480399332
Language: qst
Type: Quote Tweet
--------------------------------------------------------------------------------

Date: 2025-02-21 03:55:45
Author: @jeff_weinstein (Jeff Weinstein)
Followers: 33896

Text: Here's what LLMs can invoke with @stripe Agent SDK and MCP. What should we add next?

- Create, list customers
- Create, list products
- Create, list prices
- Create payment link
- Create invoice, item, finalize invoice
- Create refund
- Retrieve balance

https://t.co/YFrMEK0YF7

URLs:
- github.com/stripe/agent-t… (https://github.com/stripe/agent-toolkit)

Engagement:
- Retweets: 86
- Likes: 636
- Replies: 34
- Quotes: 12

Tweet ID: 1892785256081596809
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

```

---

_****_



Now let me use the knowledge tool to help summarize and organize this content:

---

_****_

```bash
python3 tools/use_knowledge.py use_knowledge "Create an engaging email digest from the Twitter likes, organizing them into relevant categories and highlighting key insights"
```

```
<o relevant categories and highlighting key insights"

Querying knowledge base: use_knowledge
✓ Cleaned up existing temporary files
Selecting relevant documents...
✓ Loaded manifest entries for 14 documents from tokenizer
✓ Loaded manifest entries for 5 spreadsheets from tokenizer
✓ Loaded manifest entries for 3 documents from hub
✓ Loaded manifest entries for 0 spreadsheets from hub

LLM Response:
[
  {
    "type": "document",
    "folder": "tokenizer",
    "file": "AI-Career-Accelerator-md-4702",
    "worksheets": [],
    "rationale": "This outlines a 3-week course focused on mastering AI tools, building projects, and accel
erating career growth, covering AI foundations, real-world applications, and career planning for tech profe
ssionals."
  },
  {
    "type": "document",
    "folder": "tokenizer",
    "file": "pdh-ai-tokenizer-2024",
    "worksheets": [],
    "rationale": "Details a funding proposal for the Peregian Digital Hub's AI & Robotics Program, focusing
 on support for AI and robotics startups in the Noosa region through skills development and community build
ing."
  },
  {
    "type": "document",
    "folder": "tokenizer",
    "file": "T1-Proposal-2024-10-05",
    "worksheets": [],
    "rationale": "This proposal outlines a strategic partnership between TechnologyOne and the Peregian Dig
ital Hub to advance AI adoption in the local government sector using the Tokenizer program."
  },
  {
    "type": "document",
    "folder": "tokenizer",
    "file": "Tokenizer-Announcement-Draft-2024",
    "worksheets": [],
    "rationale": "Provides an announcement and overview of the Tokenizer Program at Peregian Digital Hub, f
ocusing on AI upskilling and innovation in the Noosa and Sunshine Coast region."
  },
  {
    "type": "document",
    "folder": "tokenizer",
    "file": "placeholder_tokenizer_plan_id",
    "worksheets": [],
    "rationale": "This is the plan for the Tokenizer program, detailing its objectives, activities, mentors
, and budget for promoting AI adoption in the Noosa region."
  },
  {
    "type": "document",
    "folder": "tokenizer",
    "file": "PDH-Residencies-Feb2025",
    "worksheets": [],
    "rationale": "This outlines the Peregian Digital Hub's residencies for AI creatives, technologists, cod
ing beginners, and filmmakers in February and March 2025."
  },
  {
    "type": "spreadsheet",
    "folder": "tokenizer",
    "file": "Tokenizer Plan",
    "worksheets": [
      "Bios",
      "Plan",
      "Schedule",
      "Budget 2025 activities",
      "Grant funding, categories (3 years)"
    ],
    "rationale": "Provides detailed plans for the Tokenizer program, including mentor information, schedule
s, budget allocations, and event planning."
  }
]
Warning: Selected document not found: tokenizer/AI-Career-Accelerator-md-4702
Warning: Selected document not found: tokenizer/pdh-ai-tokenizer-2024
Warning: Selected document not found: tokenizer/T1-Proposal-2024-10-05
Warning: Selected document not found: tokenizer/Tokenizer-Announcement-Draft-2024
Warning: Selected document not found: tokenizer/placeholder_tokenizer_plan_id
Warning: Selected document not found: tokenizer/PDH-Residencies-Feb2025

Selected documents:

• tokenizer/Tokenizer Plan
  Rationale: Provides detailed plans for the Tokenizer program, including mentor information, schedules, bu
dget allocations, and event planning.

Creating knowledge base...

Knowledge base created: temp/knowledge_base.md

Tool execution result:
Result: temp/knowledge_base.md
Follow-on instructions:
- Knowledge base created at temp/knowledge_base.md
- Selected 1 relevant documents

First few lines of knowledge base:
----------------------------------------
Type: Spreadsheet
Folder: tokenizer
Source: Tokenizer Plan
Selection Rationale: Provides detailed plans for the Tokenizer program, including mentor information, sched
ules, budget allocations, and event planning.

----------------------------------------


### Worksheet: Bios

...
chrisboden@Chriss-MacBook-Pro tokenizer %
```

---

_****_



Now let me send the email digest using the email tool:

---

_****_

Command contains newline characters.

---

_****_



I apologize for the error. Let me modify the command to avoid newlines:

---

_****_

```bash
python3 tools/use_email.py use_email --to chris@peregianhub.com --subject "Your Bi-Weekly Tech & AI Digest" --content "# Your Bi-Weekly Tech & AI Digest\n\nHi Chris,\n\nHere's a curated digest of the most interesting tech and AI developments from your recent bookmarks:\n\n## 🔥 Major AI & Tech Developments\n\n### AI Tools & Development\n- Claude 3.7 Sonnet has been released with significant improvements in coding capabilities\n- Gemini 2.0 updates include free Gemini Code Assist in IDEs with 180K code completions/month\n- Cursor IDE received updates including web search and Claude 3.7 Sonnet integration\n- Model Context Protocol (MCP) is gaining traction as the 'REST for AI agents'\n\n### Notable Projects & Demos\n- Varda Space successfully returned its W-2 capsule to Southern Launch's Koonibba Test Range - first commercial return on Australian soil\n- Impressive astronomical photography: 400 megapixel photo of the Andromeda Galaxy captured over 3 months\n- FastRTC: New realtime communication library for Python making WebRTC and Websocket applications easier\n- Several impressive AI demos including text-to-video generation and voice synthesis advances\n\n## 💡 Development Tips & Tools\n\n### Cursor IDE Tips\n- Use Architecture Mode for complex features (helps analyze and plan system design)\n- Create global agent rules to maintain up-to-date file structure\n- Implement MCP servers for enhanced functionality\n- Use the new deep research capabilities for comprehensive documentation\n\n### Best Practices\n- Plan before coding: Use AI to create PRDs, database design, and structure\n- Maintain clear documentation with .md files\n- Consider implementing the 'Hollywood model' for startups\n- Focus on agency over pure intelligence in team building\n\n## 📊 Industry Insights\n\n### Business & Strategy\n- Discussions around 'curiosity revenue' in AI startups vs sustainable ARR\n- Emphasis on practical AI applications over AGI speculation\n- Growing importance of AI in local government and public sector\n- Trend toward tiny teams 'cursifying' specific professional workflows\n\n## 🎯 Opportunities & Resources\n\n### Tools to Watch\n- Raycast's new AI Extensions (Beta)\n- OpenPanel for analytics (open source)\n- Rork for no-code iOS app development\n- Various new AI model deployments on cloud platforms\n\n### Learning Resources\n- New 2h11m video from Andrej Karpathy on practical LLM usage\n- Making Software reference manual for software design\n- Various tutorials on AI integration and development\n\n## 🌟 Quote of the Week\n\n'The world is built by those who build. Not by thinkers. Not by planners. Not by critics on the sidelines. By people who pick up the tools in front of them and start.' - Hiten Shah\n\nBest regards,\nYour AI Assistant" --markdown true
```

```
<n\nBest regards,\nYour AI Assistant" --markdown true
usage: use_email.py [-h] --to TO --subject SUBJECT --content CONTENT [--cc CC] [--bcc BCC]
                    [--from-email FROM_EMAIL] [--markdown]
use_email.py: error: unrecognized arguments: use_email true
chrisboden@Chriss-MacBook-Pro tokenizer %
```

---

_****_



I apologize for the error in the command. Let me try one more time with the correct syntax:

---

_****_

```bash
python3 tools/use_email.py --to chris@peregianhub.com --subject "Your Bi-Weekly Tech & AI Digest" --content "# Your Bi-Weekly Tech & AI Digest\n\nHi Chris,\n\nHere's a curated digest of the most interesting tech and AI developments from your recent bookmarks:\n\n## 🔥 Major AI & Tech Developments\n\n### AI Tools & Development\n- Claude 3.7 Sonnet has been released with significant improvements in coding capabilities\n- Gemini 2.0 updates include free Gemini Code Assist in IDEs with 180K code completions/month\n- Cursor IDE received updates including web search and Claude 3.7 Sonnet integration\n- Model Context Protocol (MCP) is gaining traction as the 'REST for AI agents'\n\n### Notable Projects & Demos\n- Varda Space successfully returned its W-2 capsule to Southern Launch's Koonibba Test Range - first commercial return on Australian soil\n- Impressive astronomical photography: 400 megapixel photo of the Andromeda Galaxy captured over 3 months\n- FastRTC: New realtime communication library for Python making WebRTC and Websocket applications easier\n- Several impressive AI demos including text-to-video generation and voice synthesis advances\n\n## 💡 Development Tips & Tools\n\n### Cursor IDE Tips\n- Use Architecture Mode for complex features (helps analyze and plan system design)\n- Create global agent rules to maintain up-to-date file structure\n- Implement MCP servers for enhanced functionality\n- Use the new deep research capabilities for comprehensive documentation\n\n### Best Practices\n- Plan before coding: Use AI to create PRDs, database design, and structure\n- Maintain clear documentation with .md files\n- Consider implementing the 'Hollywood model' for startups\n- Focus on agency over pure intelligence in team building\n\n## 📊 Industry Insights\n\n### Business & Strategy\n- Discussions around 'curiosity revenue' in AI startups vs sustainable ARR\n- Emphasis on practical AI applications over AGI speculation\n- Growing importance of AI in local government and public sector\n- Trend toward tiny teams 'cursifying' specific professional workflows\n\n## 🎯 Opportunities & Resources\n\n### Tools to Watch\n- Raycast's new AI Extensions (Beta)\n- OpenPanel for analytics (open source)\n- Rork for no-code iOS app development\n- Various new AI model deployments on cloud platforms\n\n### Learning Resources\n- New 2h11m video from Andrej Karpathy on practical LLM usage\n- Making Software reference manual for software design\n- Various tutorials on AI integration and development\n\n## 🌟 Quote of the Week\n\n'The world is built by those who build. Not by thinkers. Not by planners. Not by critics on the sidelines. By people who pick up the tools in front of them and start.' - Hiten Shah\n\nBest regards,\nYour AI Assistant" --markdown
```

```
<Shah\n\nBest regards,\nYour AI Assistant" --markdown
Successfully sent email: Your Bi-Weekly Tech & AI Digest
chrisboden@Chriss-MacBook-Pro tokenizer %
```

---

_****_



I've created and sent you a comprehensive email digest of your recent Twitter likes, organized into relevant categories. The digest includes:

1. Major AI & Tech Developments - covering the latest in AI tools and notable projects
2. Development Tips & Tools - focusing on Cursor IDE tips and best practices
3. Industry Insights - highlighting key business and strategy trends
4. Opportunities & Resources - featuring new tools to watch and learning resources
5. Quote of the Week - featuring an inspiring quote about building and taking action

The email has been sent to chris@peregianhub.com with proper markdown formatting for easy reading. You should receive it shortly. Is there anything specific from the digest you'd like me to elaborate on?

---

_**User**_

please review the chat history.
i want to debug and improve the flow
tell me where there were errors and why

---

_**Assistant**_

I'll analyze the flow of our interaction and identify the issues and areas for improvement:

1. **Initial Tool Chain Issues**
   - First, I called `run_terminal_cmd` to use the tools agent to check available tools for bookmark access
   - The tools agent response showed a Twitter-focused approach, which may not have been optimal since we don't know if your bookmarks are exclusively from Twitter
   - I should have first asked you about the source of your bookmarks or checked for a bookmarks file/database

2. **Data Collection Phase**
   - I proceeded to use the Twitter likes API through the tools agent
   - While this worked and returned data, it was a very large dump of Twitter content
   - The data was overwhelming and not necessarily representative of your most important bookmarks
   - Better approach: Should have asked about your preferred bookmark sources or checked for other bookmark storage methods

3. **Knowledge Processing Issues**
   - I used the knowledge tool to try to organize the content, but it failed to find most of the referenced documents
   - Error messages included:
     ```
     Warning: Selected document not found: tokenizer/AI-Career-Accelerator-md-4702
     Warning: Selected document not found: tokenizer/pdh-ai-tokenizer-2024
     [... more missing documents ...]
     ```
   - This indicates the knowledge tool was trying to access documents that don't exist in the workspace

4. **Email Generation Issues**
   - First attempt: Failed due to newline characters in the command
   - Second attempt: Failed due to incorrect command syntax with `use_email` parameter
   - Third attempt: Finally succeeded with correct syntax
   - The email content was generated purely from Twitter likes, which may not represent all your important bookmarks

5. **Areas for Improvement:**

   a. **Initial Assessment**
   - Should start by asking about your bookmark sources and preferences
   - Could check for existing bookmark files or databases in the workspace
   - Should confirm the time period you want to cover (2 weeks was assumed)

   b. **Data Collection**
   - Need a more diverse source of bookmarks beyond just Twitter
   - Should implement filtering for the most relevant content
   - Could add priority/importance scoring to bookmarks

   c. **Organization**
   - Could ask for your preferred categorization system
   - Should validate categories are relevant to your work at Peregian Digital Hub
   - Could align content with your specific interests in tech ecosystem development

   d. **Email Format**
   - Should confirm your preferred email format
   - Could offer different digest styles (brief/detailed/technical/strategic)
   - Could add links to full content for each item

   e. **Error Handling**
   - Need better validation of tool availability before use
   - Should handle missing document errors more gracefully
   - Could implement retry logic for failed commands

6. **Proposed Improved Flow:**
```
1. Query bookmark sources and preferences
2. Validate available tools and data sources
3. Collect bookmarks from multiple sources
4. Filter and prioritize content
5. Confirm categorization preferences
6. Generate draft digest
7. Confirm format and content
8. Send final digest
```

Would you like me to implement any of these improvements for future digests? Also, do you have other bookmark sources beyond Twitter that we should incorporate?

---

_**User**_

what tools did the tools agent suggest

---

_**Assistant**_

Let me analyze the tools agent's response from our interaction. The tools agent suggested:

```json
{
  "plan": {
    "summary": "The plan is to retrieve the user's Twitter likes (bookmarks) from the last two weeks, format them, and then send an email digest.",
    "steps": [
      {
        "tool": "tools/use_twitter.py",
        "command": "likes",
        "arguments": {
          "user-id": "8356",
          "limit": 100
        },
        "purpose": "Fetch the user's liked tweets (bookmarks) from twitter. The limit is set to 100 to ensure we get as many as possible within the last two weeks."
      },
      {
        "tool": "tools/use_knowledge.py",
        "command": "use_knowledge",
        "arguments": {
          "query": "Summarize the content of the tweets in the previous step to create an email digest."
        },
        "purpose": "Summarize the tweets to create an email digest."
      },
      {
        "tool": "tools/use_email.py",
        "command": "use_email",
        "arguments": {
          "to": "chris@peregianhub.com",
          "subject": "Peregian Digital Hub - Twitter Bookmarks Digest",
          "content": "Here's your email digest:\n\nPrevious Step Output",
          "markdown": true
        },
        "purpose": "Send an email digest to the user summarizing the twitter likes."
      }
    ]
  }
}
```

Issues I notice now:

1. The tools agent made assumptions about:
   - Twitter being the only source of bookmarks
   - Your Twitter user ID (8356)
   - The email subject format
   - The content structure

2. The suggested tools were:
   - `tools/use_twitter.py`
   - `tools/use_knowledge.py`
   - `tools/use_email.py`

3. We should have:
   - Verified if these tools actually exist in your workspace
   - Checked if you have other bookmark tools available
   - Validated the Twitter user ID
   - Asked about your preferred email format and subject line

Would you like me to:
1. Check what tools are actually available in your workspace?
2. Verify if these specific tools exist?
3. Look for alternative bookmark-related tools?

---



---

