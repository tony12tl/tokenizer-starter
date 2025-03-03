## SpecStory

## Email Digest Creation from Bookmarks (02/03/2025, 21:34:53)

_**User**_

please create an engaging and detailed email digest with the things i have bookmarked over the last 2 weeks #t

---

_**Assistant**_

I notice you've used the shortcode #t which, according to the main rules, means I should check what tools are available for this task. Let me call the tools agent to help with this request.

I'll run the tools agent to see what capabilities we have for handling bookmarks and creating email digests.

---

_****_

```bash
python3 agents/tools_agent.py "create an engaging email digest from bookmarks from last 2 weeks"
```

```
python3 agents/tools_agent.py "create an engaging email digest from bookmarks from last 2 weeks"
chrisboden@Chriss-MacBook-Pro tokenizer % python3 agents/tools_agent.py "create 
an engaging email digest from bookmarks from last 2 weeks"
{
  "plan": {
    "summary": "To create an engaging email digest from bookmarks (likes) from the user's Twitter profile o
ver the last 2 weeks, I will first gather the user's liked tweets and then format that information into an 
email digest.",
    "steps": [
      {
        "tool": "tools/use_twitter.py",
        "command": "likes",
        "arguments": {
          "user-id": "8356",
          "limit": 50
        },
        "purpose": "This step retrieves the most recent liked tweets from the user's Twitter profile to gat
her content for the email digest."
      },
      {
        "tool": "tools/use_knowledge.py",
        "command": "use_knowledge",
        "arguments": {
          "query": "Create a summary of the liked tweets from the last two weeks."
        },
        "purpose": "In this step, I will format the liked tweets into a digestible summary that will be use
d in the email content."
      },
      {
        "tool": "tools/use_email.py",
        "command": "use_email",
        "arguments": {
          "to": "recipient@example.com",
          "subject": "Your Weekly Digest of Interesting Finds",
          "content": "Here is your digest of tweets you liked over the past two weeks:\n\n<!-- Include form
atted summary here -->",
          "markdown": false
        },
        "purpose": "This step sends the email digest to the specified recipient, sharing the organized and 
engaging content derived from their liked tweets."
      }
    ]
  }
}
chrisboden@Chriss-MacBook-Pro tokenizer %
```

---

_****_



I see that there are some tools available to help with this task. Let me try to use them to create your digest.

---

_****_

```bash
python3 tools/use_twitter.py likes --user-id 8356 --limit 50
```

```

Checking Twitter API credentials:
Authorization length: 111
Cookies length: 787
CSRF length: 160
Fetching likes for user ID: 8356
Response status code: 200
Request URL: https://api.twitter.com/graphql/QK8AVO3RpcnbLPKXLAiVog/Likes?variables=%7B%22userId%22%3A+%228
356%22%2C+%22count%22%3A+50%2C+%22includePromotedContent%22%3A+false%2C+%22withSuperFollowsUserFields%22%3.
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
Followers: 297252

Text: a half-hour episode of me acting with @sesame. In this first-of-its-kind art (?), we arrest a this SO
TA voice AI for drug trafficking. it is shocking how it reacts... listen!

cc @brendaniribe https://t.co/AVZPG9devw

Media:
- video: https://pbs.twimg.com/amplify_video_thumb/1895901486078476288/img/vRN_Di4QcWtFKz3_.jpg

Engagement:
- Retweets: 92
- Likes: 1040
- Replies: 156
- Quotes: 65

Tweet ID: 1895901690999824683
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-28 19:29:44
Author: @aakashg0 (Aakash Gupta)
Followers: 118007

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
- Retweets: 156
- Likes: 1505
- Replies: 13
- Quotes: 6

Tweet ID: 1895557013850992908
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-03-01 01:55:00
Author: @hnshah (Hiten Shah)
Followers: 266597

Text: The world is built by those who build.

Not by thinkers. Not by planners. Not by critics on the sidelines. By people who pick up the tools in front
 of them and start.

Michelangelo didn’t debate the best way to sculpt David. He carved. The Wright brothers didn’t seek approva
l

Engagement:
- Retweets: 143
- Likes: 747
- Replies: 34
- Quotes: 14

Tweet ID: 1895653969097015614
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-28 03:39:55
Author: @levie (Aaron Levie)
Followers: 2535073

Text: After well over a hundred years of incremental progress, all of a sudden transportation is going to c
hange very quickly https://t.co/AEgJnaL02b

Media:
- photo: https://pbs.twimg.com/media/Gk2FqZib0AAX0lV.jpg

Engagement:
- Retweets: 1465
- Likes: 9438
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
- Likes: 1237
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
Followers: 40805

Text: Python is mind-boggling for finance. 

Case in point: There's a Finance database of 300,000 tickers. 

Available 100% for free: https://t.co/wgf6B1NrQZ

Media:
- photo: https://pbs.twimg.com/media/Gk4902UXkAAxP3c.png

Engagement:
- Retweets: 198
- Likes: 1619
- Replies: 8
- Quotes: 1

Tweet ID: 1895520473733062977
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-28 20:06:27
Author: @nonzeroexitcode (daniel petho)
Followers: 2352

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
- Likes: 678
- Replies: 6
- Quotes: 1

Tweet ID: 1895566252611158370
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-28 15:00:02
Author: @basetenco (Baseten)
Followers: 3693

Text: Nobody knows what inference means but it's provocative https://t.co/hsfGdkhEv4

Media:
- video: https://pbs.twimg.com/ext_tw_video_thumb/1895485645318979585/pu/img/TzsPVc8LwET_KzeP.jpg

Engagement:
- Retweets: 66
- Likes: 841
- Replies: 88
- Quotes: 35

Tweet ID: 1895489142693429630
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-28 21:10:27
Author: @lulumeservey (Lulu Cheng Meservey)
Followers: 104025

Text: If you’re outnumbered, out of your comfort zone, and have no leverage, never never allow things to tu
rn adversarial

Engagement:
- Retweets: 110
- Likes: 2690
- Replies: 77
- Quotes: 25

Tweet ID: 1895582358679728544
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-28 19:29:03
Author: @shashj (Shashank Joshi)
Followers: 203165

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
Followers: 16792

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
Followers: 162913

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
- Likes: 4444
- Replies: 81
- Quotes: 42

Tweet ID: 1895160249364992473
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-27 19:32:40
Author: @DynamicWebPaige (👩‍💻 Paige Bailey)
Followers: 63504

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
Followers: 1207750

Text: New 2h11m YouTube video: How I Use LLMs

This video continues my general audience series. The last one focused on how LLMs are trained, so I wanted 
to follow up with a more practical guide of the entire LLM ecosystem, including lots of examples of use in
my own life.

Chapters https://t.co/urVqhSr69c

Media:
- photo: https://pbs.twimg.com/media/Gk1AYjUXoAA4bpu.jpg

Engagement:
- Retweets: 1512
- Likes: 13334
- Replies: 283
- Quotes: 169

Tweet ID: 1895242932095209667
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-27 04:44:00
Author: @tedx_ai (Ted Werbel)
Followers: 12290

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
- Likes: 210
- Replies: 6
- Quotes: 5

Tweet ID: 1895330619766219029
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-27 06:08:45
Author: @AravSrinivas (Aravind Srinivas)
Followers: 234661

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
Followers: 58222

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
Followers: 374325

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
Followers: 19698

Text: whenever you're using AI &amp; it's absolutely COOKING, send it this prompt...

"your current state is perfect, please send me a prompt in markdown format that i can send to another LLM s
o that it acts as a clone of you."

now you can send the same system prompt to every LLM you ever

Engagement:
- Retweets: 41
- Likes: 978
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
Followers: 17725

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
Followers: 12290

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
Followers: 44469

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
Followers: 47279

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
Followers: 68195

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
Followers: 238893

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
Followers: 6858016

Text: I shared this note with the Washington Post team this morning:

I’m writing to let you know about a change coming to our opinion pages. 
 
We are going to be writing every day in support and defense of two pillars: personal liberties and free mar
kets. We’ll cover other topics too

Engagement:
- Retweets: 17963
- Likes: 150106
- Replies: 27757
- Quotes: 12884

Tweet ID: 1894757287052362088
Language: en
Type: Original Tweet
--------------------------------------------------------------------------------

Date: 2025-02-24 18:29:15
Author: @gregisenberg (GREG ISENBERG)
Followers: 440326

Text: Fine, I'll say the thing that no-one is saying...

There's a bunch of AI companies with $1-10M "ARR" raising big VC money on what I'll call "curiosity revenue
" - not real sustainable ARR.

Basically, what's happening right now is a lot of people have high willingness to try AI

Engagement:
- Retweets: 105
- Likes: 1193
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
Followers: 58222

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
- Retweets: 10261
- Likes: 129143
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
Followers: 1296

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
Followers: 5528777

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
- Likes: 7378
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

```

---

_****_



Now let me use the knowledge tool to help create a summary of these tweets.

---

_****_

```bash
python3 tools/use_knowledge.py use_knowledge "Create a summary of the liked tweets from the last two weeks, organizing them into key themes and highlighting the most significant developments."
```

```
<and highlighting the most significant developments."

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
    "rationale": "Addresses the general request and provides information on AI tools and career development
 in the field."
  },
  {
    "type": "document",
    "folder": "tokenizer",
    "file": "pdh-ai-tokenizer-2024",
    "rationale": "This document describes the Tokenizer program from Peregian Digital Hub supporting innova
tion enterprises focused on AI, robotics, and automation."
  },
  {
    "type": "document",
    "folder": "tokenizer",
    "file": "T1-Proposal-2024-10-05",
    "rationale": "Details a partnership proposal focused on advancing generative AI adoption through the To
kenizer program."
  },
  {
    "type": "document",
    "folder": "tokenizer",
    "file": "Tokenizer-Announcement-Draft-2024",
    "rationale": "Provides an overview of the Tokenizer Program at PDH, its benefits, target audience, and 
key activities for AI upskilling."
  },
  {
    "type": "document",
    "folder": "tokenizer",
    "file": "placeholder_tokenizer_plan_id",
    "rationale": "Outlines the Tokenizer program plan, including objectives, activities, mentors, and budge
t for promoting AI adoption and literacy."
  },
  {
    "type": "document",
    "folder": "hub",
    "file": "noosa_coworking_spaces-20240130",
    "rationale": "Lists coworking spaces including Peregian Digital Hub, where some AI initiatives are happ
ening."
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
    "rationale": "A comprehensive plan detailing mentors, schedules, budget allocations, and activities for
 the Tokenizer program."
  }
]
Warning: Selected document not found: tokenizer/AI-Career-Accelerator-md-4702
Warning: Selected document not found: tokenizer/pdh-ai-tokenizer-2024
Warning: Selected document not found: tokenizer/T1-Proposal-2024-10-05
Warning: Selected document not found: tokenizer/Tokenizer-Announcement-Draft-2024
Warning: Selected document not found: tokenizer/placeholder_tokenizer_plan_id
Warning: Selected document not found: hub/noosa_coworking_spaces-20240130

Selected documents:

• tokenizer/Tokenizer Plan
  Rationale: A comprehensive plan detailing mentors, schedules, budget allocations, and activities for the 
Tokenizer program.

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
Selection Rationale: A comprehensive plan detailing mentors, schedules, budget allocations, and activities 
for the Tokenizer program.

----------------------------------------


### Worksheet: Bios

...
chrisboden@Chriss-MacBook-Pro tokenizer %
```

---

_****_



Let me create a digest based on the tweets I've analyzed. I'll create this in the notes directory as specified in the main rules.

---

_****_



---

_****_



---



---

