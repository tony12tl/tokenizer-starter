## SpecStory

## Debugging AI Agent Bio Query (02/03/2025, 22:34:42)

_**User**_

please run and then debug why this is not working. use this query: 'write a short bio for steve ringo for an upcoming talk he is giving on ai agents'

---

_**Assistant**_

I'll help you run and debug the `use_knowledge.py` tool. Let's start by running it with your query.

---

_****_

```bash
python3 tools/use_knowledge.py "write a short bio for steve ringo for an upcoming talk he is giving on ai agents"
```

```
python3 tools/use_knowledge.py "write a short bio for steve ringo for an upcoming talk he is giving on ai a
gents"
chrisboden@Chriss-MacBook-Pro tokenizer % python3 tools/use_knowledge.py "write 
a short bio for steve ringo for an upcoming talk he is giving on ai agents"

Querying knowledge base: write a short bio for steve ringo for an upcoming talk he is giving on ai agents
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
    "file": "Tokenizer Plan.md",
    "worksheets": [],
    "rationale": "The Tokenizer Program Plan mentions key people and their roles, providing material for a 
bio."
  },
  {
    "type": "spreadsheet",
    "folder": "tokenizer",
    "file": "Tokenizer Plan",
    "worksheets": [
      "Bios"
    ],
    "rationale": "The 'Bios' worksheet in the Tokenizer Plan spreadsheet provides biographical information 
that can be used to write a short bio."
  }
]

Selected documents:

• tokenizer/Tokenizer Plan.md
  Rationale: The Tokenizer Program Plan mentions key people and their roles, providing material for a bio.

• tokenizer/Tokenizer Plan
  Rationale: The 'Bios' worksheet in the Tokenizer Plan spreadsheet provides biographical information that 
can be used to write a short bio.

Creating knowledge base...

Knowledge base created: temp/knowledge_base.md

Tool execution result:
Result: temp/knowledge_base.md
Follow-on instructions:
- Knowledge base created at temp/knowledge_base.md
- Selected 2 relevant documents

First few lines of knowledge base:
----------------------------------------
Type: Document
Folder: tokenizer
Source: Tokenizer Plan.md
Selection Rationale: The Tokenizer Program Plan mentions key people and their roles, providing material for
 a bio.

----------------------------------------

# **What is it**

#
...
chrisboden@Chriss-MacBook-Pro tokenizer %
```

---

_****_



It seems there might be an issue with the environment configuration. Let me check a few things:

1. First, let's verify if the `DESTINATION_FOLDER` environment variable is set correctly.
2. Let's check if the required directory structure exists.

---

_****_

<details>
            <summary>Listed current directory • **14** results</summary>
        
| Name |
|-------|
| 📁 `temp` |
| 📁 `notes` |
| 📁 `.git` |
| 📁 `agents` |
| 📁 `tools` |
| 📄 `email_digest.md` |
| 📄 `.gitignore` |
| 📁 `knowledge` |
| 📄 `.env` |
| 📁 `memory` |
| 📁 `.cursor` |
| 📁 `evals` |
| 📁 `instructions` |
| 📁 `.specstory` |

</details>

---

_****_



Let me check the `.env` file to see if the `DESTINATION_FOLDER` is properly configured:

---

_****_

Read file: .env

---

_****_



I can see several issues:

1. The `DESTINATION_FOLDER` in the `.env` file is set to `/Users/chrisboden/Dropbox/knowledgebase`, but based on the script's output, it seems to be looking in the `tokenizer` and `hub` folders.

2. The script is finding manifest entries (14 documents from tokenizer, 5 spreadsheets from tokenizer, 3 documents from hub), but it's not able to properly access the content.

Let's check if the knowledge directory exists and has the expected structure:

---

_****_

<details>
            <summary>Listed directory knowledge • **1** results</summary>
        
| Name |
|-------|
| 📄 `llms.txt` |

</details>

---

_****_



I see several issues that need to be fixed:

1. The `DESTINATION_FOLDER` in the `.env` file points to a different location than where the script is finding the manifests.
2. The knowledge directory structure doesn't match what the script expects (it's looking for subdirectories like `tokenizer` and `hub` with `documents` and `spreadsheets` subdirectories).

Here's what we need to do to fix this:

1. First, let's check if the actual knowledge base exists at the configured location:

---

_****_

```bash
ls -la /Users/chrisboden/Dropbox/knowledgebase
```

```
chrisboden@Chriss-MacBook-Pro tokenizer % ls -la /Users/chrisboden/Dropbox/knowledgebase
total 88
drwxr-xr-x@  7 chrisboden  staff    224 Mar  1 23:02 .
drwx------@ 35 chrisboden  staff   1120 Mar  2 12:58 ..
-rw-r--r--@  1 chrisboden  staff   6148 Feb 12 05:09 .DS_Store
drwxr-xr-x@  3 chrisboden  staff     96 Mar  1 20:35 .specstory
drwxr-xr-x@  5 chrisboden  staff    160 Mar  1 23:02 hub
-rw-r--r--@  1 chrisboden  staff  33426 Mar  1 23:03 llms.txt
drwxr-xr-x@  5 chrisboden  staff    160 Mar  1 23:02 tokenizer
chrisboden@Chriss-MacBook-Pro tokenizer %
```

---

_****_



Great! I can see that the knowledge base directory exists and has the correct structure with `hub` and `tokenizer` directories. Let's check the structure of one of these directories:

---

_****_

```bash
ls -la /Users/chrisboden/Dropbox/knowledgebase/tokenizer
```

```
chrisboden@Chriss-MacBook-Pro tokenizer % ls -la /Users/chrisboden/Dropbox/knowledgebase/tokenizer
total 8
drwxr-xr-x@  5 chrisboden  staff   160 Mar  1 23:02 .
drwxr-xr-x@  7 chrisboden  staff   224 Mar  1 23:02 ..
-rw-r--r--@  1 chrisboden  staff  1596 Mar  2 22:12 .sync_state.json
drwxr-xr-x@ 18 chrisboden  staff   576 Mar  2 22:11 documents
drwxr-xr-x@  9 chrisboden  staff   288 Mar  1 23:00 spreadsheets
chrisboden@Chriss-MacBook-Pro tokenizer %
```

---

_****_



Now I can see that the directory structure is correct, with `documents` and `spreadsheets` subdirectories. The script is finding the manifests but seems to be having trouble accessing the actual files.

Let's check if we can access one of the manifest files:

---

_****_

```bash
cat /Users/chrisboden/Dropbox/knowledgebase/tokenizer/documents/@manifest.json
```

```
[
  {
    "id": "AI-Career-Accelerator-md-4702",
    "title": "AI Career Accelerator",
    "fileName": "Tokenizer Course.md",
    "localPath": "path/to/your/documents",
    "createdAt": "2024-01-01T00:00:00+00:00",
    "updatedAt": "2025-03-01T20:31:51+00:00",
    "summary": "The AI Career Accelerator is a 3-week cohort-based course focused on mastering AI tools, bu
ilding projects, and accelerating career growth. It covers AI foundations, real-world applications, and car
eer planning, with a focus on durable human skills. The course is designed for tech professionals, leaders,
 and career advancers.",
    "wordCount": 1419,
    "source": "Markdown File",
    "language": "en",
    "primaryTopics": [
      "Artificial Intelligence",
      "Career Development",
      "Technology",
      "Professional Skills",
      "AI Tools"
    ],
    "questionTypes": [],
    "useCases": [
      "career planning",
      "skill development",
      "AI integration strategies",
      "product management",
      "engineering workflows",
      "entrepreneurship"
    ],
    "audience": "Tech professionals, product managers, engineers, data scientists, UX/UI designers, tech le
aders, C-suite executives, startup founders, and career changers interested in AI.",
    "documentSections": [
      {
        "sectionTitle": "COURSE OVERVIEW",
        "summary": "This section provides an introduction to the course, highlighting the importance of AI 
skills and the need for a structured approach to learning AI."
      },
      {
        "sectionTitle": "The Goal",
        "summary": "This section describes the intended outcomes of the course, including foundational AI k
nowledge, hands-on skills, and development of durable human skills."
      },
      {
        "sectionTitle": "How We'll Get There",
        "summary": "This section outlines the methodology and key components of the course, such as hands-o
n experience, personal skill assessment, real-world applications, and project-based learning."
      },
      {
        "sectionTitle": "What sets this course apart",
        "summary": "This section highlights the unique aspects of the course, including its focus on both A
I fluency and durable human skills, interactive sessions, and personalized feedback."
      },
      {
        "sectionTitle": "Who is this course for?",
        "summary": "This section defines the target audience for the course, including tech professionals, 
leaders, founders, and career advancers."
      },
      {
        "sectionTitle": "What you'll get out of this course",
        "summary": "This section lists the specific benefits and skills participants will gain, such as ide
ntifying AI quick wins, building a repeatable assessment, and developing a career plan."
      },
      {
        "sectionTitle": "Course syllabus",
        "summary": "This section provides a detailed breakdown of the course schedule and topics covered ea
ch week."
      },
      {
        "sectionTitle": "Meet your instructor",
        "summary": "This section introduces Nate Jones, the instructor, highlighting his experience and phi
losophy on AI and career development."
      },
      {
        "sectionTitle": "Join an upcoming cohort",
        "summary": "This section provides information on upcoming course dates, cost, and enrollment detail
s."
      },
      {
        "sectionTitle": "Learning is better with cohorts",
        "summary": "This section describes the benefits of cohort-based learning, including active hands-on
 learning, interactive projects, and a supportive community."
      },
      {
        "sectionTitle": "Frequently Asked Questions",
        "summary": "This section addresses common questions about the course, such as time commitment, refu
nd policy, and suitability for different backgrounds."
      }
    ],
    "fileType": "document",
    "about": "This document is a course overview and syllabus for the AI Career Accelerator, designed to he
lp tech professionals and leaders integrate AI into their careers and workflows.",
    "questionsAnswered": [
      "how-to integrate AI into my career?",
      "what AI skills are most valuable?",
      "why is AI fluency important?",
      "what are the best AI tools for productivity?",
      "how-to future-proof my career with AI?",
      "what skills make a career durable in the age of AI?"
    ],
    "contentHash": "44d26b82cc30ae4ffaa96735ff73dcea"
  },
  {
    "id": "doc_-1389644171259123475",
    "title": "Tokenizer - RDA",
    "fileName": "Tokenizer - RDA.md",
    "localPath": "/Users/chrisboden/Dropbox/knowledgebase/tokenizer/documents",
    "createdAt": "2025-03-01T21:25:42.874626+00:00",
    "updatedAt": "2025-03-01T21:25:42.874626+00:00",
    "summary": "",
    "wordCount": 2874,
    "source": "Google Docs",
    "language": "en",
    "primaryTopics": [],
    "questionTypes": [],
    "useCases": [],
    "audience": "general",
    "documentSections": [],
    "contentHash": "9fef58b48584e49abe301b5f89165f5f"
  },
  {
    "id": "pdh-ai-tokenizer-2024",
    "title": "Tokenizer: Peregian Digital Hub AI & Robotics Program",
    "fileName": "Tokenizer Notes.md",
    "localPath": "./",
    "createdAt": "2024-05-03T00:00:00+00:00",
    "updatedAt": "2024-05-03T00:00:00+00:00",
    "summary": "The Peregian Digital Hub is seeking funding to enhance support for AI and robotics startups
 in the Noosa region, addressing the unique challenges they face. The program aims to attract, nurture, and
 accelerate the growth of these specialized IDEs through various initiatives, including skills development,
 community building, and access to resources.",
    "wordCount": 3463,
    "source": "Grant Application Document",
    "language": "en",
    "primaryTopics": [
      "Artificial Intelligence",
      "Robotics",
      "Innovation",
      "Startup Ecosystem",
      "Economic Development",
      "Skills Development"
    ],
    "questionTypes": [],
    "useCases": [
      "proposal evaluation",
      "strategic planning",
      "program development",
      "investment analysis",
      "ecosystem building"
    ],
    "audience": "Government funding bodies, investors, regional stakeholders, tech startups, innovation hub
s, and economic development agencies.",
    "documentSections": [
      {
        "sectionTitle": "Short Program Activity Description",
        "summary": "This section introduces the Peregian Digital Hub's funding request to support innovatio
n-driven enterprises (IDEs) in the Noosa region, with a focus on AI, robotics, and automation. It highlight
s the importance of generative AI and the need for dedicated support to attract and nurture startups."
      },
      {
        "sectionTitle": "Significance of the Funding Opportunity",
        "summary": "This section explains how the funding opportunity over the next three years will extend
 the Peregian Digital Hub's current service offering to the region. It emphasizes leveraging the emergence
of generative AI to drive innovation and establish the Hub as a leading center for AI in Australia."
      },
      {
        "sectionTitle": "Relevance of Additional Services",
        "summary": "This section describes the relevance of additional services to support innovation for I
DEs in the region. It focuses on mentorship, market access, lean startup development, and best practices to
 encourage the development of new solutions and economic growth."
      },
      {
        "sectionTitle": "Impact, Outputs, and Outcomes",
        "summary": "This section details the expected impact, outputs, and outcomes from the additional ser
vice offering over the next three years including BASE, NURTURE, UPSKILL, and LAB programs. It emphasizes e
ncouraging new solutions, creating jobs, and strengthening the Sunshine Coast's reputation as an innovation
 hub."
      },
      {
        "sectionTitle": "Year 1",
        "summary": "This section outlines the program activities scheduled for Year 1, focusing on attracti
ng and identifying AI & Robotics startups, accelerating new startups, developing the AI talent base, and pr
oductizing living lab facilities for robotics activities. It includes specific actions like outbound market
ing, mentoring, and skills development programs."
      },
      {
        "sectionTitle": "Year 2",
        "summary": "This section details the program activities for Year 2, building upon Year 1 with refin
ed marketing strategies, expanded AI Founder Network, hosting more advanced workshops, and making the robot
ics lab operational. It includes specific actions like targeted outreach, specialised AI courses, and hands
-on projects."
      },
      {
        "sectionTitle": "Year 3",
        "summary": "This section outlines the program activities for Year 3, focusing on sustaining the gro
wth of AI & Robotics startups, continuing to expand the AI Founder Network, evolving skills development pro
grams, and fully operationalizing the Robotics Living Lab. It includes actions like developing targeted out
reach strategies and expanding workshops."
      },
      {
        "sectionTitle": "Organisation\u2019s Track Record",
        "summary": "This section summarizes the Peregian Digital Hub\u2019s track record over the past 12 m
onths in delivering services to the innovation ecosystem. It highlights the Hub's support for startups, hos
ting of events and workshops, and delivery of skills development programs, demonstrating a commitment to fo
stering a thriving tech ecosystem."
      },
      {
        "sectionTitle": "Organisation\u2019s Capability, Resourcing, Knowledge, Skills and Experience",
        "summary": "This section outlines the Peregian Digital Hub's capability to deliver the proposed gen
erative AI program. It highlights the Hub's dedicated team, state-of-the-art facilities, strong network of
mentors, and a proven track record in supporting AI and robotics companies."
      },
      {
        "sectionTitle": "Value for Money",
        "summary": "This section explains why the proposed program represents value for money in terms of o
utcomes and impact for Queensland. It emphasizes the Hub's track record of generating significant returns o
n investment, targeted skills development, and amplification of regional impact."
      },
      {
        "sectionTitle": "Risks and Mitigation",
        "summary": "This section identifies the risks to delivering the program activities within time and 
budget, including staff capacity, mentor availability, and startup take-up. It proposes mitigation strategi
es like identifying additional resources, key mentors, and widening marketing reach."
      },
      {
        "sectionTitle": "Sustainability and Resilience",
        "summary": "This section outlines how the Peregian Digital Hub\u2019s operations are sustainable an
d resilient over the next three years. It emphasizes the Hub's diversified revenue stream, strong foundatio
n of support from Noosa Shire Council, and proven track record of navigating challenges."
      },
      {
        "sectionTitle": "Connections and Networks",
        "summary": "This section explains how the funding opportunity will support the Peregian Digital Hub
 to establish connections and networks that support its growth beyond the three years of funding. It focuse
s on attracting new partners, expanding reach, developing a strong AI network, and building a talent pipeli
ne."
      },
      {
        "sectionTitle": "Program Activities",
        "summary": "This section provides a table summarizing proposed program activities, including attrac
ting and identifying AI & Robotics startups to the region, accelerating startups, developing the AI talent
base, and providing facilities for AI & Robotics. It includes details on when, how, and who is involved in
these activities."
      },
      {
        "sectionTitle": "Period 1 - Activities",
        "summary": "This section lists the activities scheduled for the first 12-month reporting period, fo
cusing on attracting and identifying AI & Robotics startups, accelerating new startups, developing the AI t
alent base, and creating a prospectus and model for the Robotics Living Lab."
      },
      {
        "sectionTitle": "Period 1 - Outcomes",
        "summary": "This section outlines the expected outcomes achieved during the first 12-month reportin
g period, including attracting qualified inquiries, identifying startups already operating in the region, e
stablishing a dedicated AI Founder Network, raising awareness about AI, and securing EOIs for the Robotics
Living Lab."
      },
      {
        "sectionTitle": "Period 2 - Activities",
        "summary": "This section lists the activities scheduled for the second 12-month reporting period, b
uilding upon Year 1 activities with refined strategies, expanding the AI Founder Network, hosting advanced
workshops, and making the robotics lab operational"
      },
      {
        "sectionTitle": "Period 2 - Outcomes",
        "summary": "This section lists the outcomes expected in period 2, including startups setting up on 
the Coast with Hub assistance, expansion of the AI Founder Network, mentor support for new startups, increa
sed numbers at workshops focused on developing an AI talent base, and companies making successful use the r
obotics lab."
      },
      {
        "sectionTitle": "Period 3 - Activities",
        "summary": "This section lists the activities scheduled for the third 12-month reporting period, in
cluding targeted outreach, partnership for the Robotics Lab, mentoring and expanded founder networks, and h
ackthons to build the skills base."
      },
      {
        "sectionTitle": "Period 3 - Outcomes",
        "summary": "This section lists the outcomes expected in period 3, including new jobs, thriving and 
successful AI startups in an expanded network that attracts investment and supports AI/Robotics skills deve
lopment and opportunities"
      }
    ],
    "fileType": "document",
    "about": "This document is about a funding proposal by the Peregian Digital Hub to develop a program su
pporting innovation-driven enterprises (IDEs) in the Noosa region, focusing on AI, robotics, and automation
. It details the program's activities, expected outcomes, and the Hub's capabilities.",
    "questionsAnswered": [
      "why invest in AI and robotics startups?",
      "how to support innovation in a regional tech ecosystem?",
      "how-to create a successful AI and robotics program?",
      "what are the key elements of a thriving startup ecosystem?",
      "what is the economic impact of investing in AI and robotics?",
      "how to attract and retain talent in the tech industry?"
    ],
    "contentHash": "92027bbf1800662b7741ffbdde554867"
  },
  {
    "id": "T1-Proposal-2024-10-05",
    "title": "A Strategic Partnership for Mutual Growth in the Age of AI",
    "fileName": "T1 Proposal.md",
    "localPath": "./",
    "createdAt": "2024-10-04T00:00:00+00:00",
    "updatedAt": "2024-10-04T00:00:00+00:00",
    "summary": "This proposal outlines a partnership opportunity between TechnologyOne and the Peregian Dig
ital Hub to advance generative AI adoption in the local government sector through the Tokenizer program. It
 details benefits, contributions, and potential outcomes for both parties, as well as community and economi
c impacts.",
    "wordCount": 1897,
    "source": "Peregian Digital Hub",
    "language": "en",
    "primaryTopics": [
      "Generative AI",
      "Partnerships",
      "Local Government",
      "Technology Innovation",
      "Economic Development"
    ],
    "questionTypes": [],
    "useCases": [
      "proposal evaluation",
      "strategic planning",
      "partnership development",
      "investment decisions",
      "community engagement"
    ],
    "audience": "TechnologyOne executives, Peregian Digital Hub stakeholders, local government officials, A
I startups, tech community members",
    "documentSections": [
      {
        "sectionTitle": "Background",
        "summary": "This section gives background information on the prior relationship between TechOne and
 Noosa council, as well as details the Peregian Digital Hub's current activities in the AI space."
      },
      {
        "sectionTitle": "Tokenizer Program Overview",
        "summary": "This section describes the Tokenizer program, a multi-faceted program designed to accel
erate the growth of generative AI capability within the Sunshine Coast region, detailing its four key pilla
rs: expanding the AI & Robotics Startup Base, accelerating Startup Growth, Developing the AI Talent Base, a
nd enhancing Robotics Lab faciities."
      },
      {
        "sectionTitle": "Partnership Overview",
        "summary": "This section introduces the partnership between Peregian Digital Hub and TechOne, highl
ighting the contributions expected from each party."
      },
      {
        "sectionTitle": "Peregian Digital Hub Contribution",
        "summary": "This section outlines the contributions the Hub will make to the partnership, including
 professional development opportunities, facility usage, partner attribution, connections with AI startups,
 and marketing initiatives."
      },
      {
        "sectionTitle": "TechOne Contribution",
        "summary": "This section specifies the financial contribution requested from TechnologyOne ($125,00
0 per annum for three years) to expand the scope and reach of the Tokenizer program."
      },
      {
        "sectionTitle": "Potential Benefits to TechOne",
        "summary": "This section details the potential benefits for TechnologyOne, including access to AI k
nowledge, skills development, enhanced innovation through startup connections, and a strengthened brand rep
utation."
      },
      {
        "sectionTitle": "Draft Press Release and FAQ\u2019s",
        "summary": "This section includes a draft press release announcing the partnership and a list of fr
equently asked questions about the Tokenizer program and the partnership."
      },
      {
        "sectionTitle": "Peregian Digital Hub: A Leading Force in AI",
        "summary": "This section highlights the Peregian Digital Hub's existing AI initiatives and resource
s, including the AI Cadetship Program, Coding from Beach events, the Upstream program, and partnerships wit
h major tech companies."
      }
    ],
    "fileType": "document",
    "about": "This document is a partnership proposal from Peregian Digital Hub to TechnologyOne. It outlin
es how TechnologyOne can strategically partner with the Peregian Digital Hub to leverage generative AI with
in the local government sector through the 'Tokenizer' program. It details the program's goals, the benefit
s to both parties, and a draft press release.",
    "questionsAnswered": [
      "how to foster a partnership between a tech hub and a software company",
      "why generative AI is important for local government",
      "what are the benefits of investing in AI talent and startups",
      "how can a company enhance its brand reputation through community engagement",
      "what are the key components of a successful AI program"
    ],
    "contentHash": "75a3e8783e1accd2598a5dfe985f083a"
  },
  {
    "id": "Tokenizer-Announcement-Draft-2024",
    "title": "Tokenizer Announcement",
    "fileName": "Tokenizer Announcement Draft.md",
    "localPath": "./",
    "createdAt": "2024-01-01T00:00:00+00:00",
    "updatedAt": "2024-01-01T00:00:00+00:00",
    "summary": "The Tokenizer Program at Peregian Digital Hub is designed to empower individuals and busine
sses in the Noosa region with AI skills and support. The program offers workshops, mentoring, networking, a
nd access to facilities, targeting various groups from tech startups to community members.",
    "wordCount": 1482,
    "source": "Peregian Digital Hub",
    "language": "en",
    "primaryTopics": [
      "Artificial Intelligence",
      "Upskilling",
      "Community Development",
      "Digital Innovation",
      "Technology Education"
    ],
    "questionTypes": [],
    "useCases": [
      "attracting investment in AI startups in the Noosa region",
      "upskilling digital professionals in AI",
      "developing AI-powered solutions for local industries",
      "fostering a tech community focused on AI and Robotics",
      "career switching in the AI field"
    ],
    "audience": "Tech startups, digital professionals, SME leaders, community members, and anyone intereste
d in AI and its applications in the Noosa and Sunshine Coast region.",
    "documentSections": [
      {
        "sectionTitle": "Tokenizer Announcement",
        "summary": "This section introduces the Tokenizer program as an initiative by Peregian Digital Hub 
to help the community adapt, learn, and thrive with AI through shared learning and action."
      },
      {
        "sectionTitle": "Who is Tokenizer For?",
        "summary": "This section outlines the various cohorts that the Tokenizer program is designed for, i
ncluding Hub members, AI startups, digital marketers, digital creatives, technologists, non-exec directors,
 teenagers, kids, SME leaders, knowledge professionals, local government, and the Noosa community."
      },
      {
        "sectionTitle": "FAQ",
        "summary": "This section answers common questions about getting involved, costs, schedules, materia
l availability, program organizers, and mentors."
      },
      {
        "sectionTitle": "Tokenizer Membership",
        "summary": "This section introduces the Tokenizer Program Membership, highlighting its benefits for
 growing AI skills and shaping the future of technology."
      },
      {
        "sectionTitle": "Peregian Digital Hub Launches Tokenizer Program Membership: Upskilling Noosa for t
he Age of AI \ud83d\ude80",
        "summary": "This sections focuses on the importance of equipping Noosa individuals and businesses w
ith the required skills, guidance, community, and facilities to prosper in this new age of AI, robotics, an
d digital transformation."
      },
      {
        "sectionTitle": "Frequently Asked Questions (FAQ) - Tokenizer Program",
        "summary": "This section provides comprehensive answers to common questions about the Tokenizer Pro
gram, covering the mission, vision, eligibility, activities, benefits, funding, and future impact of the pr
ogram."
      },
      {
        "sectionTitle": "Tokenizer Program for Members",
        "summary": "This section describes the schedule of events available to members of the Tokenizer Pro
gram, breaking down the events by what skills they teach, how they inspire, how to ideate, and opportunitie
s for show and tell."
      },
      {
        "sectionTitle": "February",
        "summary": "This section describes the 'Upstream' event for February, which teaches a hands-on intr
oduction to Cursor and how to work with agents."
      },
      {
        "sectionTitle": "March",
        "summary": "This section outlines the schedule of Tokenizer events occurring in March. These includ
e an 'Upstream' session, an 'Inspire' session, an 'Ideate' session, and a 'Show & Tell' session. Each event
 has a distinct goal."
      },
      {
        "sectionTitle": "April",
        "summary": "This section outlines the schedule of Tokenizer events occurring in April. Similar to M
arch, the events include an 'Upstream' session, an 'Inspire' session, an 'Ideate' session, and a 'Show & Te
ll' session. Each event has a distinct goal."
      }
    ],
    "fileType": "document",
    "about": "This document is an announcement and detailed overview of the Tokenizer Program at Peregian D
igital Hub, an initiative focused on AI upskilling and fostering innovation within the Noosa and Sunshine C
oast region. It outlines program benefits, target audiences, and key activities, while also answering frequ
ently asked questions about the program and membership.",
    "questionsAnswered": [
      "what is the Tokenizer Program?",
      "who is the Tokenizer Program for?",
      "how can I get involved in the Tokenizer Program?",
      "what activities are available through Tokenizer?",
      "why is AI important for the Noosa region?"
    ],
    "contentHash": "bbe54cc0f69974b761fd911ec1cb23f6"
  },
  {
    "id": "placeholder_tokenizer_plan_id",
    "title": "Tokenizer Program Plan",
    "fileName": "Tokenizer Plan.md",
    "localPath": "/documents/tokenizer",
    "createdAt": "2024-10-27T10:00:00+00:00",
    "updatedAt": "2024-10-27T10:00:00+00:00",
    "summary": "The Tokenizer program aims to boost AI adoption in the Noosa region by focusing on startups
, SMBs, professionals, and the community. It involves education, mentoring, and proof-of-concept developmen
t, supported by a network of mentors and funded by the Queensland Government's Advance QLD initiative. The
program seeks to address both the opportunities and threats of AI by upskilling participants and fostering
innovation.",
    "wordCount": 1406,
    "source": "Markdown File",
    "language": "en",
    "primaryTopics": [
      "Artificial Intelligence",
      "Digital Hub",
      "Upskilling",
      "Mentoring",
      "Startup Support",
      "Community Development",
      "Economic Development"
    ],
    "questionTypes": [],
    "useCases": [
      "Regional economic development planning",
      "Technology skills gap analysis",
      "Curriculum development for AI education",
      "Startup ecosystem building",
      "Government grant proposal writing"
    ],
    "audience": "Regional development stakeholders, educators, AI startups, SMEs, professionals",
    "documentSections": [
      {
        "sectionTitle": "What is it",
        "summary": "This section outlines the target audiences and the activities planned for each group, i
ncluding startups, marketers, creatives, technologists, non-executive directors, teenagers, kids, SMEs, pro
fessionals, and local government. It details the specific initiatives such as peer networks, workshops, res
idencies, hackathons, cadetship programs, and inventor clubs, tailored to each group's needs."
      },
      {
        "sectionTitle": "Mentors",
        "summary": "This section lists the mentors involved in the Tokenizer program and their contribution
s, covering areas like AI basics, prompting, automation, PoC development, startup mentoring, enterprise sup
port, technical support, and venture mentoring. It also mentions mentors for specific areas like CS fundame
ntals, LLM, prompting, and AI tools."
      },
      {
        "sectionTitle": "Objective",
        "summary": "This section describes the main objective of the Tokenizer program: making the region a
n AI hotspot by attracting, identifying, and supporting startups, educating and supporting SMBs and profess
ionals, and educating the community and kids in AI-related skills through various programs and initiatives.
"
      },
      {
        "sectionTitle": "Tokenizer Recap",
        "summary": "This section provides a recap of the Tokenizer program, explaining its origins as an in
itiative of the Peregian Digital Hub supported by the Queensland Government\u2019s Advance QLD initiative.
It highlights the program's goal of helping the region navigate the opportunities and challenges presented
by AI, including supporting startups, enabling SMBs, and upskilling professionals."
      },
      {
        "sectionTitle": "Approach",
        "summary": "This section details the approach of the Tokenizer program, which involves providing AI
 exposure and upskilling support to medium-sized enterprises, offering 1:1 commercial mentoring, and suppor
ting the development of AI proof of concepts to validate surfaced ideas."
      },
      {
        "sectionTitle": "Recruitment of Participants",
        "summary": "This section describes the recruitment process for the Tokenizer program, which involve
s working closely with organizations like the Chamber of Commerce, Food and Agribusiness Network, Manufactu
ring Excellence Forum, Tourism Noosa, Council, and the RDA to identify businesses that would benefit from t
he program and inviting them to participate via Expression of Interest."
      },
      {
        "sectionTitle": "Mentors",
        "summary": "This section gives more details on the mentors and their bios involved in the Tokenizer
 program, including Steve Telburn as the stream lead, Rom\u00e1n Olivera as the automation mentor, Deborah
van der Vlist and Michael Ridland as PoC tech mentors, and Ian Hansel and Oscar Lloyd as PoC tech mentors,
detailing their expertise and contributions to the program."
      },
      {
        "sectionTitle": "Expenditure Overview",
        "summary": "This section breaks down the budget allocation for the SMB stream of the Tokenizer prog
ram, detailing the expenditure on marketing, upskilling, commercial mentoring, and PoC support, with specif
ic percentages allocated to each category."
      },
      {
        "sectionTitle": "Tokenizer Program: Simplified Framework",
        "summary": "This section simplifies the Tokenizer program into three core pillars: attract, nurture
, and upskill. It maps the proposed activities to these pillars and further abstracts them into scalable pr
ogram components such as ecosystem development, talent pipeline, startup acceleration, and living lab acces
s, outlining key actions for scalable delivery."
      }
    ],
    "fileType": "document",
    "about": "This document is a plan for the Tokenizer program, an initiative by the Peregian Digital Hub 
to promote AI adoption and literacy in the Noosa region. It outlines the program's objectives, target audie
nces, activities, mentors, and budget, aiming to make the region an AI hotspot and support startups, SMBs,
professionals, and the community through education, mentoring, and proof-of-concept development.",
    "questionsAnswered": [
      "what is the tokenizer program?",
      "how-to promote AI adoption in a region?",
      "why support AI literacy?",
      "how-to create an AI startup ecosystem?"
    ],
    "contentHash": "d554af5c76bcaf9b39d2a71dc5422ae6"
  },
  {
    "id": "PDH-Residencies-Feb2025",
    "title": "Peregian Digital Hub Residencies - February/March 2025",
    "fileName": "Hub Residencies Feb 25.md",
    "localPath": "./",
    "createdAt": "2024-10-26T00:00:00+00:00",
    "updatedAt": "2024-10-26T00:00:00+00:00",
    "summary": "The Peregian Digital Hub is hosting residencies in February and March 2025 for AI creatives
, technologists, coding beginners, and filmmakers. The document outlines the purpose, objectives, and benef
its of these residencies, highlighting opportunities for mentorship and collaboration.",
    "wordCount": 344,
    "source": "Local Disk",
    "language": "en",
    "primaryTopics": [
      "Digital Hub",
      "Residencies",
      "Filmmaking",
      "AI",
      "Technology",
      "Education"
    ],
    "questionTypes": [],
    "useCases": [
      "promoting residency programs",
      "attracting filmmakers and technologists to the Sunshine Coast",
      "facilitating collaboration and knowledge-sharing"
    ],
    "audience": "Filmmakers, technologists, AI creatives, coding beginners, and the Sunshine Coast screen i
ndustry",
    "documentSections": [
      {
        "sectionTitle": "Residency for AI Creatives",
        "summary": "This section outlines a residency program for creatives on the Sunshine Coast intereste
d in learning how to use AI tools in their work, featuring Esther De Schoene and Hing An of Aesop Media as
mentors."
      },
      {
        "sectionTitle": "Residency for Technologists",
        "summary": "This section introduces a residency program for technologists, featuring Jeff Bowen, a 
former Facebook engineer."
      },
      {
        "sectionTitle": "Residency for Coding Beginners",
        "summary": "This sections introduces a residency program for coding beginners featuring Oscar Lloyd
, mechatronics engineer and tech educator as the resident."
      },
      {
        "sectionTitle": "Residency for filmmakers",
        "summary": "This document is about a residency program for filmmakers, featuring Bettina Dalton fro
m WildBear Entertainment as the resident, focusing on providing mentorship and consultations to develop doc
umentary projects."
      },
      {
        "sectionTitle": "Residency Overview",
        "summary": "This a high level summary of Bettina Dalton's residency including her credentials as an
 Emmy- and Sundance-nominated Producer and Filmmaker, WildBear Entertainment."
      },
      {
        "sectionTitle": "About Bettina Dalton",
        "summary": "This section provides the professional background of Bettina Dalton, highlighting her a
ccomplishments and projects in documentary filmmaking."
      },
      {
        "sectionTitle": "Purpose and Objectives",
        "summary": "This section describes the aims of the filmmaker residency, focusing on mentorship, col
laboration within the Sunshine Coast documentary filmmaking community, and positioning the Peregian Digital
 Hub as a center for creative development."
      },
      {
        "sectionTitle": "Expected Benefits",
        "summary": "This section details the anticipated advantages of the filmmaker residency for filmmake
rs, the Sunshine Coast screen industry, and the region."
      }
    ],
    "fileType": "document",
    "about": "This document is about the Peregian Digital Hub's residencies for February and March 2025, fo
cusing on AI creatives, technologists, coding beginners, and filmmakers. It details the residency programs,
 mentors, objectives, and expected benefits.",
    "questionsAnswered": [
      "what residencies are being offered at the Peregian Digital Hub?",
      "who is Bettina Dalton and what is her role in the filmmaker residency?",
      "how can filmmakers benefit from the residency program?",
      "how to book a session with Bettina Dalton?"
    ],
    "contentHash": "090c119f556242b07a31f7953072087d"
  },
  {
    "id": "placeholder-unique-id-1",
    "title": "New Test Doc",
    "fileName": "new test doc.md",
    "localPath": "/path/to/documents/",
    "createdAt": "2024-01-01T00:00:00+00:00",
    "updatedAt": "2024-01-01T00:00:00+00:00",
    "summary": "A simple test document created to validate the metadata extraction tool.",
    "wordCount": 6,
    "source": "Markdown Editor",
    "language": "en",
    "primaryTopics": [
      "testing",
      "documentation"
    ],
    "questionTypes": [],
    "useCases": [
      "testing metadata extraction pipeline"
    ],
    "audience": "Developers, QA engineers",
    "documentSections": [
      {
        "sectionTitle": "Document Body",
        "summary": "This section contains the main textual content of the document; in this case, it's just
 a sentence identifying it as a test document."
      }
    ],
    "fileType": "document",
    "about": "This document is a basic test document to demonstrate the functionality of the metadata extra
ction process. It contains a title and a placeholder image reference.",
    "questionsAnswered": [
      "what is a test document?"
    ],
    "contentHash": "5b7ae9ace875e08f3bef1fd1b88feaca"
  },
  {
    "id": "ec9b2265",
    "title": "Test Document",
    "fileName": "Test_Document_1740823574_ec9b2265.md",
    "localPath": ".",
    "createdAt": "2025-03-01T20:06:14+00:00",
    "updatedAt": "2025-03-01T20:06:14+00:00",
    "summary": "A test document designed to evaluate document creation functionality with a unique identifi
er, creation timestamp, and some test data.",
    "wordCount": 30,
    "source": "Google Docs",
    "language": "en",
    "primaryTopics": [
      "Document Creation Testing"
    ],
    "questionTypes": [],
    "useCases": [
      "software testing",
      "quality assurance"
    ],
    "audience": "Software Testers",
    "documentSections": [
      {
        "sectionTitle": "Purpose",
        "summary": "This section describes the purpose of the document, which is to test the creation of ne
w documents in Google Drive."
      },
      {
        "sectionTitle": "Test Data",
        "summary": "This section provides test data in the form of a list of items for testing purposes."
      },
      {
        "sectionTitle": "Unique Identifier",
        "summary": "This section specifies the unique identifier for the document, which is 'ec9b2265'."
      }
    ],
    "fileType": "document",
    "about": "This document is a test document created to evaluate the document creation process within Goo
gle Drive.",
    "questionsAnswered": [
      "how-to create documents"
    ],
    "contentHash": "6cafffbedc0ca80a8dc52121a2406786"
  },
  {
    "id": "5b3629f3",
    "title": "Test Document",
    "fileName": "Test_Document_1740823606_5b3629f3.md",
    "localPath": ".",
    "createdAt": "2025-03-01T20:06:46+00:00",
    "updatedAt": "2025-03-01T20:06:46+00:00",
    "summary": "A test document created in Google Drive to test document creation functionality. Contains a
 brief description, test data, and a unique ID.",
    "wordCount": 37,
    "source": "Google Docs",
    "language": "en",
    "primaryTopics": [
      "document creation",
      "testing",
      "Google Drive"
    ],
    "questionTypes": [],
    "useCases": [
      "software testing",
      "system validation"
    ],
    "audience": "Software developers, quality assurance engineers",
    "documentSections": [
      {
        "sectionTitle": "Purpose",
        "summary": "This section explains the goal of creating the document, which is to test new document 
creation capabilities in Google Drive."
      },
      {
        "sectionTitle": "Test Data",
        "summary": "This section presents example test data in a list format, serving as placeholder conten
t for testing the document creation process."
      },
      {
        "sectionTitle": "Unique Identifier",
        "summary": "This section declares the unique identifier of the document. It helps in distinguishing
 it from other tested documents in Google Drive."
      }
    ],
    "fileType": "document",
    "about": "This document is a test document created to evaluate the functionality of creating new docume
nts within Google Drive. It includes a purpose statement, sample test data, and a unique identifier for tra
cking.",
    "questionsAnswered": [
      "how-to create a test document",
      "why use test data?"
    ],
    "contentHash": "e678e9cb06b4b1953d0973c2af82e231"
  },
  {
    "id": "vjqctxbd",
    "title": "Test Document 20250301_194804",
    "fileName": "test_20250301_194804_vjqctxbd.md",
    "localPath": ".",
    "createdAt": "2025-03-01T19:48:04.075240+00:00",
    "updatedAt": "2025-03-01T19:48:15.653724+00:00",
    "summary": "This is a test document created to verify the two-way sync and update functionalities of a 
system using the test_sync.py script.",
    "wordCount": 49,
    "source": "test_sync.py",
    "language": "en",
    "primaryTopics": [
      "testing",
      "synchronization",
      "update functionality"
    ],
    "questionTypes": [],
    "useCases": [
      "system testing",
      "software development",
      "quality assurance"
    ],
    "audience": "Software developers, QA engineers",
    "documentSections": [
      {
        "sectionTitle": "Test Section",
        "summary": "This section describes the creation of the document by the test_sync.py script for veri
fying two-way sync functionality."
      },
      {
        "sectionTitle": "Update Test",
        "summary": "This section describes the document update functionality test and the modification time
stamp."
      }
    ],
    "fileType": "document",
    "about": "This document is a test document used to verify the two-way sync functionality of a system. I
t includes sections created at different times to test the update functionality.",
    "questionsAnswered": [
      "how-to verify sync functionality",
      "how-to test document updates"
    ],
    "contentHash": "8995ac1fdbc1a54c87a0a1a8384effc1"
  },
  {
    "id": "osohcick",
    "title": "Test Document 20250301_194424",
    "fileName": "test_20250301_194424_osohcick.md",
    "localPath": ".",
    "createdAt": "2025-03-01T19:44:24.201529+00:00",
    "updatedAt": "2025-03-01T19:44:35.870433+00:00",
    "summary": "This is a test document automatically generated to verify the two-way sync functionality, i
ncluding the update functionality, of a script.",
    "wordCount": 42,
    "source": "test_sync.py script",
    "language": "en",
    "primaryTopics": [
      "software testing",
      "synchronization",
      "script verification"
    ],
    "questionTypes": [],
    "useCases": [
      "software development",
      "quality assurance",
      "script debugging"
    ],
    "audience": "developers, quality assurance engineers",
    "documentSections": [
      {
        "sectionTitle": "Test Section",
        "summary": "This section describes the purpose of the test document which is to verify the two-way 
sync functionality."
      },
      {
        "sectionTitle": "Update Test",
        "summary": "This section confirms that an update was successfully made, thereby testing the update 
functionality."
      }
    ],
    "fileType": "document",
    "about": "This document is a test document created to verify the functionality of a two-way sync script
, specifically testing both creation and update functionalities.",
    "questionsAnswered": [
      "how to verify sync functionality",
      "how to test update functionality"
    ],
    "contentHash": "1976a7de02d3d86a2e533654984ef551"
  },
  {
    "id": "ypybbirh",
    "title": "Test Document 20250301_193911",
    "fileName": "test_20250301_193911_ypybbirh.md",
    "localPath": ".",
    "createdAt": "2025-03-01T19:39:11.304924+00:00",
    "updatedAt": "2025-03-01T19:39:58.085130+00:00",
    "summary": "This test document verifies the two-way sync functionality and update functionality of a sy
stem.",
    "wordCount": 42,
    "source": "test_sync.py script",
    "language": "en",
    "primaryTopics": [
      "software testing",
      "synchronization",
      "update functionality"
    ],
    "questionTypes": [],
    "useCases": [
      "system integration testing",
      "bug verification",
      "qa testing"
    ],
    "audience": "software developers, QA engineers, system administrators",
    "documentSections": [
      {
        "sectionTitle": "Test Section",
        "summary": "This section describes the purpose of the test document, which is to verify the two-way
 sync functionality."
      },
      {
        "sectionTitle": "Update Test",
        "summary": "This section contains content that was added later to test the update functionality of 
the sync process."
      }
    ],
    "fileType": "document",
    "about": "This document is a test case generated by a Python script to validate the two-way synchroniza
tion feature, including content updates.",
    "questionsAnswered": [
      "how-to verify sync functionality",
      "how-to test document updates"
    ],
    "contentHash": "dcdd05dd71abbd59325402c74bfcc208"
  },
  {
    "id": "xdkrqsfk",
    "title": "Test Document 20250301_214720",
    "fileName": "test_20250301_214720_xdkrqsfk.md",
    "localPath": ".",
    "createdAt": "2025-03-01T21:47:20.559959+00:00",
    "updatedAt": "2025-03-01T21:47:28.894905+00:00",
    "summary": "A test document designed to validate the two-way sync functionality and update mechanisms."
,
    "wordCount": 44,
    "source": "test_sync.py script",
    "language": "en",
    "primaryTopics": [
      "testing",
      "synchronization",
      "software development"
    ],
    "questionTypes": [],
    "useCases": [
      "software testing",
      "development workflow verification"
    ],
    "audience": "developers, QA engineers",
    "documentSections": [
      {
        "sectionTitle": "Test Section",
        "summary": "This section describes the document's purpose as a test for two-way synchronization."
      },
      {
        "sectionTitle": "Update Test",
        "summary": "This section tests the update functionality by adding content after the initial documen
t creation."
      }
    ],
    "fileType": "document",
    "about": "This document is a test document created to verify the two-way sync functionality. It include
s sections for initial creation and updates.",
    "questionsAnswered": [
      "how-to verify sync functionality"
    ],
    "contentHash": "2ce0ebb2393cf4732422fcea0dc8a58c"
  }
]%


```

---

_****_



Based on the investigation, I can see that the script is working as expected in terms of:
1. Finding the knowledge base directory
2. Reading the manifests
3. Selecting relevant documents

However, there seems to be an issue with accessing the actual document content. Let's check if we can access one of the selected documents:

---

_****_

```bash
cat "/Users/chrisboden/Dropbox/knowledgebase/tokenizer/documents/Tokenizer Plan.md"
```

```
# **What is it**

# 

|  |  |
| :---- | :---- |
| AI Startups | Peer network, regular founder events, best practice sharing |
| Marketers | Workshops & talks for upskilling |
| Creatives | Residencies, workshops & talks for upskilling |
| Technologists | Residencies, Hackathon, Workshops & talks for upskilling |
| Non Exec Directors | Workshops |
| Teenagers | AI Cadetship program |
| Kids | Inventor Club |
| SME’s |  |
| Professionals | Workshops & talks for upskilling |
| Local government | Key staff upskilling |

# **Mentors**

| Mentor | Contribution |
| :---- | :---- |
| Chris Boden | Basics |
| Megan Fawdon | Prompting |
| Steve Ringo | Automation |
| Roman Olivera | Automation |
|  |  |
|  |  |
| Ian Hansel | PoC Development |
| Greg Freeman |  |
| Duncan Hoggan |  |
| Michael Ridland | PoC Development |
|  |  |
|  |  |
| Dale Rankine | Startup mentoring |
| Aaron Blackman | Startup mentoring |
| Raeleen Kaesehagen | Enterprise support |
| Steve Telburn | Enterprise support |
|  |  |
| Luc Pettett | Exemplar |
| Pip Bingemann | Exemplar |
| Andrew Birt | Exemplar |
| Dale Rankine | Exemplar |
| Kris Owens | Exemplar |
|  |  |
| Oscar Lloyd | Technical support |
| Noah Moller | Youth program |
|  |  |
| Steve Telburn | Venture mentor |
| Craig Manson | Venture mentor |
| Rob Easton | Angel mentor |
| Vinko Grgic | Angel mentor |
|  |  |

Rocks to Intelligence

| CS Fundamentals | Malte von Ruden |  |
| :---- | :---- | :---- |
| Oscar Lloyd |  |  |
| LLM |  |  |
| Prompting |  |  |
| Tools | ChatGPT, NotebookLM, AI Studio, Zapier, Perplexity |  |

| Cohort | Activities | Outcomes |
| :---- | :---- | :---- |
| SMB’s |  |  |
| NED’s |  |  |
| Hub members |  |  |
| Creatives |  |  |
| Technologists |  |  |
| Youth |  |  |

**Objective**

Make the region an AI hotspot

- Startups (Attract, Identify, Support)  
    
  - AI Founders network


- SMB’s (Educate, Support)  
    
  - Focus on 10-20 medium size employers  
  - Mentoring support with aim to get to PoC  
  - Identify via Hub outreach/Chamber/MEF/FAN


- Professionals (Educate)  
    
  - Coding from Beach  
      
    - Developing with AI  
    - Hackathons

  - ## **Reboot**

  - SCSC  
      
    - AI Creative support  
      - Residency  
      - Workshops


- Community (Educate)  
    
  - Digital Leaders via Library  
  - Content


- Kids (Educate)  
    
  - Inventor Club  
  - AI Cadetship  
  - Holiday Program


- High level of AI literacy

## **Tokenizer Recap**

The Peregian Digital Hub is a public service initiative of the Noosa Council with a mandate to help build o
ut a vibrant digital sector in the region that helps bolster and diversify the local economy and, through i
ts activities, contributes to building social capital in our community.

The Hub believes that AI is likely to have a seismic impact on our region’s economy and community in the ne
ar term and that it must move quickly and proactively to deliver programs that will help the region navigat
e the opportunities and challenges that are coming.

The Tokenizer program is a modest attempt to do that. It builds on a series of experimental programs that h
ave been run at the Hub through 2023 and 2024 as AI was finding its feet with early adopters.

With funding support from the Queensland Government’s Advance QLD initiative, the Tokenizer program is an a
ttempt to put the region on the front foot with respect to AI.

Much like the internet and smartphone before it, AI is a general purpose technology that allows people and 
businesses to do things that were not previously possible.

This creates opportunity for new value creation:

* Startups can bring entirely new products and services to market that were never before possible.  
* Existing SMB’s can develop new products or services that are uniquely enabled by AI; or they can improve 
their efficiency or profitability by using AI and/or robotics for automation.
* Professionals can learn the skills related to this new technology, and make themselves more employable.

To realise these opportunities, startups, businesses and professionals all need to wrap their heads around 
this new technology and upskill so that they have the knowledge needed to unlock those new opportunities.

The newness of the technology and the speed at which it is evolving means that there are very few experts. 
No-one has 5 years experience working with generative AI,, because it is only 24 months old.

In contrast to the opportunities, there is the real threat that existing SMB’s that fail to leverage this t
echnology will be out-competed by those that do. And we must not wave away the likely disruption that AI wi
ll have on white-collar professionals. Much of that is outside of our control but what we can do is try to
ensure that our region is as well-informed and prepared as it can be, so that it benefits from this technol
ogy shift and does not get left behind.

The Tokenizer program aims to lift awareness about the opportunities that AI brings, and to help participan
ts by inspiring them, upskilling them and supporting them.

The RDA support would allow us to include SMB’s in the program and would fund specific activities aimed at 
that cohort.

## **Approach**

The approach is to try to provide AI exposure and upskilling support to a significant number of medium size
 enterprises in the region so that they can take those learnings and immediately implement some of the best
 practices in their organisations.

For a subset of those organisations, we will provide 1:1 commercial mentoring, to dig into specific opportu
nities and use cases for their business. This involves a more consultative approach and will benefit from t
he expertise of a mentor with significant experience helping organisations unlock commercial value from the
ir IP.

Finally, a smaller group of participants will be supported through developing an AI proof of concept, that 
would aim to validate that the ideas that were surfaced through the mentoring process, can be executed and
would deliver the intended value.

|  | \~30 participants |
| :---: | :---- |
|  | \~12 participants shortlisted |
|  | \~5 PoC’s supported |
|  |  |
|  |  |

## **Recruitment of Participants**

The Hub will work closely with the Chamber of Commerce, Food and Agribusiness Network, Manufacturing Excell
ence Forum, Tourism Noosa, Council and the RDA itself, to identify the businesses in the region that would
best benefit from the program and generate prospects via EOI.

Partners will be provided collateral and messaging to share the program opportunity with those prospects, a
s well as do our own outreach and marketing to reach companies that would best benefit from Tokenizer.

At this point, we believe that the Upskill offering can provide a valuable starting point for many business
es in the region, and the more intensive 1:1 mentoring and PoC opportunities should be thoughtfully allocat
ed to businesses that would best benefit, and, commit to, bringing a PoC to life and validating its potenti
al.

## **Mentors**

This stream will be led by Steve Telburn, a highly experienced CEO, commercialisation mentor, advisor and v
enture partner.

Steve will draw on other mentors from the Tokenizer bench, on-demand, as the participants are qualified and
 selected, and their specific needs and opportunities are better understood.

Our view is that this stream of activities will generate the most value if it results in proof of concept e
xecutions that help the participating companies actualise the value that AI and automation can bring to the
ir businesses.

| Mentor | Bio |
| :---- | :---- |
| Steve Telburn *Stream Lead* | Steve Telburn is a seasoned CEO and venture partner with extensive experien
ce in guiding deep-tech startups from inception to profitability, exit, or failure, often supported by Seri
es A funding from leading Australian venture capital firms. With a background in pharmacology and psycholog
y from Monash University, he has successfully led five startups, leveraging artificial intelligence, machin
e learning, and automation to drive revenue growth and cost reduction for clients. As a venture partner at
Antler, he facilitates the growth of emerging businesses, while his advisory roles in organizations like Ex
ercise & Sports Science Australia enhance strategic planning and governance in the healthcare sector. In ad
dition to his entrepreneurial ventures, Steve has played a pivotal role in public funding initiatives, havi
ng contributed to the allocation of over $500 million in startup innovation grants across Australia. His le
adership at Secret Sauce Technology Ventures and participation in various boards, including Industry Innova
tion and Science Australia, showcase his commitment to fostering innovation and commercialization in the te
ch ecosystem. Steve's multifaceted expertise positions him as a valuable mentor in the Tokenizer program, w
here he can help local startups and SMBs unlock new value through adoption of AI and robotics. |
| Roman Olivera
               *Automation mentor* | Román Olivera. is a seasoned entrepreneur and co-founder of EVEN Labs,
 a company that delivers innovative health and fitness solutions through its online platform for corporate
clients and endurance athletes. With a BSc in Mechanical and Electrical Engineering from Tecnológico de Mon
terrey, Román has a robust background in project management, having previously held key roles at General El
ectric and led operations as COO at Power Engineering Services and Solutions (PESS). His experience spans a
cross strategic, financial, and operational aspects of business, equipping him with a holistic understandin
g of various industries, particularly in energy and technology. Román has developed deep expertise in busin
ess process automation via AI for small-medium-scale businesses and has helped a number of companies at the
 Hub with those best practices. |
| Deb van der Vlist
                   PoC tech mentor | Deborah van der Vlist is a skilled Website Developer and Graphic Desig
ner based in Peregian Beach, Queensland, Australia. With a Certificate III in Information Technology from T
AFE Queensland, she specializes in creating visually appealing and functional websites across various platf
orms including Jekyll, WordPress, Shopify, and Webflow. Deborah has contributed her expertise to several pr
ojects as a Frontend Developer at G Factor Technologies and has also excelled in freelance roles through he
r own venture, WebVdev, focusing on web development and UI/UX design. Deborah is an expert in rapid prototy
ping and has supported a number of Hub companies bring their product ideas to life in a lean, fast and effi
cient way. |
| Michael Ridland *PoC tech mentor* | Michael Ridland is a seasoned technology leader with over 20 years of
 experience in software development, specializing in AI, enterprise applications, and digital solutions. As
 the Chief Technologist and co-founder of XAM Consulting, he successfully led a team that grew from 2 to 85
 professionals, delivering award-winning projects for clients such as Kmart and Telstra. Michael’s expertis
e in generative AI consulting is evidenced by his work with early adopters, resulting in five customers and
 multiple case studies. A seven-time Microsoft MVP, he has shared his knowledge at over 30 international co
nferences, enhancing the tech community's understanding of AI and software development. Currently, Michael
is focused on consulting for AI products and services, leveraging his extensive skill set that includes Azu
re, AWS, and OpenAI technologies. Michael is a very accomplished technologist and has been building generat
ive AI products since the availability of LLMs. His ability to understand business requirements and rapidly
 build new products using the latest tech stack, is a valuable asset in the Tokenizer program. |
| Ian Hansel
            *PoC tech mentor* | Ian Hansel is a seasoned data scientist and the Director at Verge Labs, whe
re he leads innovative projects focused on the applied side of machine learning. With a Bachelor's degree i
n Advanced Mathematics (Honours) from the University of Wollongong and further training in Practical Deep L
earning from The University of Queensland, Ian possesses a robust foundation in statistical modeling and pr
edictive analytics. His career highlights include redesigning a modeling tool for price optimization at a l
eading consumer product research company and evaluating the causal impact of promotional campaigns at Calte
x Australia. Ian's experience as a Data Science Instructor at General Assembly, where he taught various dat
a science courses, showcases his dedication to education and skill development. Ian was an early adopter of
 generative AI technologies and has worked with a number of clients including Hub members, to help them har
ness AI in their products and services. His data science background is extremely valuable to the program in
 terms of assisting companies with interesting data-centric assets that could unlock new value.. |
| Oscar Lloyd
             *PoC tech mentor* | Oscar Lloyd is a passionate mechatronics and physics student at The Univer
sity of Queensland, specializing in robotics and AI. As the Founder of ProxiTech, he develops innovative AI
 and robotics applications for the manufacturing and service sectors, while also offering educational servi
ces in collaboration with the Peregian Digital Hub and RoboCoast. Oscar has led and executed complex projec
ts, including AI-powered robotic systems, and is recognized for his critical thinking and collaborative ski
lls.His achievements include winning first place at the UQMARS Microcontroller Hackathon and the UQMARS Ard
uino Hackathon, along with being a recipient of the prestigious UQ Academic Excellence Scholarship. Oscar's
 contribution to the Tokenizer program will be helpful in supporting SMBs that could unlock new value throu
gh embracing AI and robotics solutions. |
| Other | Through the ​​Peregian Digital Hub’s network of members, founders, partners and supporters, the T
ok
enizer program has a large bench of talented people and subject-matter experts at its disposal. As the need
s of particular participants become more apparent, the program will be able to draw on specialised contribu
tors, as required. |

**Expenditure Overview**

The RDA contribution would be directed towards this SMB stream of the Tokenizer program. We envision alloca
ting the funding to these activities

| Category | Description | Budget |
| :---- | :---- | :---- |
| Marketing | Expenditure to find and recruit participants | 10% |
| Upskilling | Expenditure to support the education component of this stream | 20% |
| Commercial mentoring | Expenditure on mentoring support provided by Stream Lead | 50% |
| PoC support | Expenditure on mentoring support provided by technical expert who can assist with PoC devel
opment | 20% |

Tokenizer Program: Simplified Framework

Instead of getting lost in the weeds of individual activities, let's think in terms of core program pillars
. Based on your proposal and the RDA information, here's a simplified framework:

I. Core Pillars:

We can essentially distill the Tokenizer program into three core pillars:

1. Attract: Bring in new AI & Robotics startups and talent to the region.  
2. Nurture: Support the growth and development of existing startups and founders.  
3. Upskill: Develop the broader AI talent pool within the region (including existing businesses).

II. Mapping Activities to Pillars:

Now, let's map the proposed activities from your grant application to these pillars:

| Pillar | Activity | Simplified Description | Scalability |
| :---- | :---- | :---- | :---- |
| Attract | Outbound marcomms, Prospectus, Storytelling, Concierge inbound EoI’s | Targeted Outreach & Mark
eting \- Promote Noosa as an AI hub | Moderate \- Requires targeted effort but can be amplified through dig
ital channels and partnerships. |
|  | Identify unknown, latent and potential AI & Robotics startups already in the region | Regional Talent 
Scouting \- Find existing players | High \- Leverage existing networks (Chamber, other orgs) and online pla
tforms to identify potential. |
| Nurture | Zero to one startup mentoring, AI founder network, Needs-based mentor matchmaking | Mentorship 
& Founder Support \- Provide guidance, resources, and connections | Moderate \- Relies on mentor availabili
ty but can be structured with group sessions and online resources. |
| Upskill | Build awareness of AI opportunity set & need for skills | AI Awareness Campaigns \- Broad outre
ach to educate about AI's potential | High \- Can leverage online platforms, webinars, and partnerships for
 broad reach. |
|  | Gather EOI’s | Interest Capture & Pipeline Building \- Collect data, identify skill gaps | High \- Aut
omated forms and online platforms can streamline this. |
|  | Offer Classes, Workshops, Hackathons | Skills Development Programs \- Hands-on training, workshops, an
d practical application | Moderate to High \- Scalable through online delivery, partnerships with training
providers, and train-the-trainer models. |
| Lab | a project to productise living lab facilities for Robotics activities, building on initial living l
ab prototype developed through Firetech Connect program | Robotics Living Lab \- Provide access to equipmen
t and facilities | Moderate \- Requires initial investment but can be scaled through memberships and usage
fees. |
|  | Prospectus, membership model, stakeholder support, delivery model | Develop Lab Resources & Framework 
\- Create materials, processes and partnerships | High \- Once developed, these can be reused and adapted f
or different projects. |

III. Simplifying for Scalability:

Now, let's abstract these further into scalable program components:

1. Ecosystem Development: This encompasses "Attract" and aspects of "Nurture" and "Upskill". Think of it as
 building the overall environment for AI to thrive.
   * Activities: Targeted outreach, marketing, community building, networking events, relationship building
 with other regional bodies, establishing partnerships.
   * Scalability: High \- leveraging digital channels, partnerships, and creating repeatable event formats.

2. Talent Pipeline: This focuses on the "Upskill" pillar, creating a skilled workforce.  
   * Activities: Workshops, courses, hackathons, cadetships, online training, mentorship programs.  
   * Scalability: High \- Can leverage online platforms, train-the-trainer models, and partnerships with ed
ucational institutions.
3. Startup Acceleration: This is the core of "Nurture", providing direct support to startups.  
   * Activities: Mentorship, founder network, workshops tailored to startup needs (fundraising, scaling, et
c.), connections to investors and partners.
   * Scalability: Moderate \- Requires curated matching and expert input, but can be structured with cohort
 models and online resources.
4. Living Lab Access: This is your "Lab" pillar, providing crucial physical and technical resources.  
   * Activities: Providing access to equipment, facilities, technical expertise, and testing environments. 

   * Scalability: Moderate \- Dependent on physical space and equipment, but can be scaled through membersh
ips, partnerships, and tiered access models.

IV. Key Actions for Scalable Delivery:

1. Develop Standardized Program Modules: Create core modules for workshops, courses, and mentorship program
s that can be adapted and reused.
2. Build a Strong Online Presence: Leverage a robust website, social media, and online platforms to deliver
 content, attract participants, and foster community engagement.
3. Train the Trainer: Develop a program to train mentors and instructors, expanding your capacity to delive
r programs.
4. Partnerships: Collaborate with other organizations (universities, industry groups, etc.) to leverage the
ir resources and expertise.
5. Data-Driven Approach: Track key metrics (participation rates, satisfaction, job creation, etc.) to measu
re impact, identify areas for improvement, and demonstrate value to stakeholders.
6. Phased Rollout: Start with core offerings and gradually expand based on demand and available resources. 
Prioritise based on the immediate needs of the ecosystem and demonstrated interest.

Example Email to Jacki Steel:

Subject: Re: Regional Enablers \- REP013-2024RD1 \- Noosa Shire Council \- Funding Agt Draft Schedule 1 for
 revision

Hi Jacki,

Thanks so much for the positive feedback from the RDAMBSC Board on our Tokenizer proposal. We're thrilled t
o have their support and are eager to move forward with delivering this impactful program.

We understand the Board's request for further detail, and we're happy to provide that. I've attached a more
 detailed breakdown of the proposed budget, outlining the specific activities and associated costs. I've al
so included information on the AI experts, educators, and mentors we have on board, along with their releva
nt credentials. Finally, you'll find a set of specific KPIs we will use to track the program's progress and
 measure its success, including target numbers for workshops, participants, and new AI projects initiated. 
I'm available for a preliminary discussion tomorrow between 1:30 PM and 3:00 PM, or alternatively, next Mon
day between 2:30 PM and 3:30 PM. Please let me know which time works best for you and your colleague, and I
'll arrange a meeting room.

We are confident that the Tokenizer program will be a significant asset to the Sunshine Coast's growing tec
h ecosystem, and we're committed to working closely with RDAMBSC to ensure its success. We look forward to
discussing the proposal further with you.

Regards,  
Chris Boden  
Director, Peregian Digital Hub

Marketing  

```

---

_****_



Now I can see that we can access the document content. Let's check the spreadsheet content as well:

---

_****_

```bash
ls -la "/Users/chrisboden/Dropbox/knowledgebase/tokenizer/spreadsheets/Tokenizer Plan"
```

```
chrisboden@Chriss-MacBook-Pro tokenizer % ls -la "/Users/chrisboden/Dropbox/knowledgebase/tokenizer/spreads
heets/Tokenizer Plan"                     ls -la "/Users/chrisboden/Dropbox/knowledgebase/tokenizer/spreads
heets/Tokenizer Plan"
total 96
drwxr-xr-x@ 7 chrisboden  staff    224 Feb 11 20:32 .
drwxr-xr-x@ 9 chrisboden  staff    288 Mar  1 23:00 ..
-rw-r--r--@ 1 chrisboden  staff  29854 Mar  2 22:33 Bios.csv
-rw-r--r--@ 1 chrisboden  staff   3393 Mar  2 22:33 Budget 2025 activities.csv
-rw-r--r--@ 1 chrisboden  staff   1277 Mar  2 22:33 Grant funding, categories (3 years).csv
-rw-r--r--@ 1 chrisboden  staff    177 Mar  2 22:33 Plan.csv
-rw-r--r--@ 1 chrisboden  staff   2069 Mar  2 22:33 Schedule.csv
chrisboden@Chriss-MacBook-Pro tokenizer %
```

---

_****_





Let's check the Bios.csv file since that's what the LLM selected:

---

_****_

```bash
cat "/Users/chrisboden/Dropbox/knowledgebase/tokenizer/spreadsheets/Tokenizer Plan/Bios.csv"
```

```
Mentor,Linkedin,Contribution,Biography
Chris Boden,https://www.linkedin.com/in/chrisboden/,Basics,"Chris Boden is the Digital Hub Director at Noos
a Shire Council, where he is instrumental in cultivating a thriving digital ecosystem in Noosa, Australia.
With extensive experience as a tech executive and entrepreneur, Chris has a rich history of leading innovat
ions in mobile technology, including his pivotal role at Lonely Planet, where he spearheaded the developmen
t of groundbreaking mobile applications. These apps were featured at the launch of the iPhone App Store and
 iPad, significantly contributing to Lonely Planet's status as the leading travel publisher on mobile platf
orms.

Before his tenure at Lonely Planet, Chris co-founded several startups, including Wenzani and TripChum, and 
served as CEO of MIG China, establishing it as a top mobile games publisher in the region. His entrepreneur
ial spirit, combined with a passion for emerging technologies, positions Chris as a valuable mentor within
the Tokenizer program, where he aims to foster innovation and support local startups navigating the rapidly
 evolving landscape of AI and robotics."
Megan Fawdon,https://www.linkedin.com/in/megan-fawdon-ab3b5a97/,Prompting,"Megan Fawdon is a seasoned Finan
cial Controller and CPA, currently serving as the Finance & Operations Manager at Telescope AI. With a rich
 background spanning diverse industries, including gambling, television, and non-profits, Megan has honed h
er expertise in navigating complex financial landscapes while embracing the dynamic world of AI technology.
 Renowned for her mastery of finance functions—ranging from payroll and financial reporting to budgeting an
d forecasting—Megan is a tech-savvy professional who thrives on optimizing operations through innovative so
lutions."
Steve Ringo,https://www.linkedin.com/in/stevenringo/,Automation,"Steven Ringo is a seasoned technology exec
utive, currently serving as the Vice President of IT & Security at Epiminder, a leading biotechnology firm
focused on developing innovative EEG recorders for epilepsy monitoring. With a strong foundation in electri
cal engineering and an MSc in Engineering Management from the University of the Witwatersrand, Steven bring
s over two decades of diverse experience in software architecture, cloud solutions, and AI-driven technolog
ies. He has successfully led transformative projects at prestigious organizations, including Amazon Web Ser
vices, where he guided software businesses in modernizing their applications and adopting cloud solutions. 
Throughout his career, Steven has been instrumental in architecting scalable systems and implementing best 
practices in cloud computing, particularly within regulated environments like healthcare. As a mentor in th
e Tokenizer program, he will leverage his extensive expertise in AI and software development to empower sta
rtups and SMBs in the Sunshine Coast region, fostering innovation and driving economic growth. His commitme
nt to upskilling local talent and enhancing technological capabilities aligns perfectly with the program's
vision, making him a valuable asset to the Tokenizer initiative."
Roman Olivera,https://www.linkedin.com/in/romanolivera/,Automation,"Román Olivera. is a seasoned entreprene
ur and co-founder of EVEN Labs, a company that delivers innovative health and fitness solutions through its
 online platform for corporate clients and endurance athletes. With a BSc in Mechanical and Electrical Engi
neering from Tecnológico de Monterrey, Román has a robust background in project management, having previous
ly held key roles at General Electric and led operations as COO at Power Engineering Services and Solutions
 (PESS). His experience spans across strategic, financial, and operational aspects of business, equipping h
im with a holistic understanding of various industries, particularly in energy and technology. Román's expe
rtise in fostering startups and his commitment to mentorship will significantly enhance the Tokenizer progr
am, empowering local businesses to leverage AI and robotics for growth and innovation."
Deb van der Vlist,https://www.linkedin.com/in/vdevphotography/,PoC Development,"Deborah van der Vlist is a 
skilled Website Developer and Graphic Designer based in Peregian Beach, Queensland, Australia. With a Certi
ficate III in Information Technology from TAFE Queensland, she specializes in creating visually appealing a
nd functional websites across various platforms including Jekyll, WordPress, Shopify, and Webflow. Deborah
has contributed her expertise to several projects as a Frontend Developer at G Factor Technologies and has
also excelled in freelance roles through her own venture, WebVdev, focusing on web development and UI/UX de
sign. Deborah's involvement in the Tokenizer program will be invaluable as she mentors startups and SMBs in
 leveraging AI and technology for enhanced digital presence, driving innovation and effective user engageme
nt within the community."
Ian Hansel,https://www.linkedin.com/in/ian-hansel/,PoC Development,"Ian Hansel is a seasoned data scientist
 and the Director at Verge Labs, where he leads innovative projects focused on the applied side of machine
learning. With a Bachelor's degree in Advanced Mathematics (Honours) from the University of Wollongong and
further training in Practical Deep Learning from The University of Queensland, Ian possesses a robust found
ation in statistical modeling and predictive analytics. His career highlights include redesigning a modelin
g tool for price optimization at a leading consumer product research company and evaluating the causal impa
ct of promotional campaigns at Caltex Australia.

Ian's experience as a Data Science Instructor at General Assembly, where he taught various data science cou
rses, showcases his dedication to education and skill development. His contributions to the Tokenizer progr
am will be invaluable as he mentors startups and SMBs in harnessing AI-driven solutions, leveraging his ext
ensive industry knowledge to foster innovation within the Noosa region."
Michael Ridland,https://www.linkedin.com/in/michaelridland/,PoC Development,"Michael Ridland is a seasoned 
technology leader with over 20 years of experience in software development, specializing in AI, enterprise
applications, and digital solutions. As the Chief Technologist and co-founder of XAM Consulting, he success
fully led a team that grew from 2 to 85 professionals, delivering award-winning projects for clients such a
s Kmart and Telstra. Michael’s expertise in generative AI consulting is evidenced by his work with early ad
opters, resulting in five customers and multiple case studies. A seven-time Microsoft MVP, he has shared hi
s knowledge at over 30 international conferences, enhancing the tech community's understanding of AI and so
ftware development.

Currently, Michael is focused on consulting for AI products and services, leveraging his extensive skill se
t that includes Azure, AWS, and OpenAI technologies. His commitment to innovation and mentorship aligns per
fectly with the Tokenizer program, where he will provide invaluable guidance to startups and SMBs looking t
o harness the power of AI and robotics to transform their businesses."
Greg Freeman,https://www.linkedin.com/in/gfreeau/,Tech mentor,"Greg Freeman is an accomplished technology e
xecutive and three-time Chief Technology Officer, boasting over 20 years of experience in aligning technolo
gy strategy with business objectives across diverse sectors, including enterprise SaaS, health tech, and fi
ntech. He has a proven track record of driving significant commercial impact, exemplified by leading teams
to achieve a remarkable 3x valuation growth within two years and contributing to a successful exit exceedin
g $100 million. His leadership capabilities extend internationally, managing engineering teams in Australia
, Germany, Canada, and the USA, while adeptly transforming underperforming teams into high-functioning unit
s focused on secure, scalable solutions.

Currently serving as an Advisor and CTO at the Peregian Digital Hub, Greg is dedicated to fostering innovat
ion and growth among startups. His deep expertise in cloud technologies, AI, and machine learning positions
 him as a vital resource for the Tokenizer program. Greg's passion for exploring how AI will reshape busine
ss models and careers, paired with his strategic insight, will significantly enhance the program's goals of
 driving economic growth and community development in the Noosa region."
Duncan Hoggan,https://theorg.com/org/luca-app/org-chart/duncan-hoggan,Tech mentor,"Duncan Hoggan is a Senio
r Backend Engineer at luca, bringing over a decade of experience in software engineering. He began his care
er at GfK as a Junior Engineer in 2012, advancing to Engineer in 2013. In 2014, he joined Emerge Mobile, in
itially as a Junior Engineer and later as an Android Software Engineer. From 2015 to 2022, Duncan served as
 a Software Engineer at Nologo Studios. He then became the Lead Software Engineer at The Delta in 2022, a r
ole he held until 2023. Duncan earned his Bachelor of Engineering (BSc.Eng.) in Electronic Engineering from
 the University of KwaZulu-Natal, where he studied from 2006 to 2011.

In the Tokenizer program, Duncan's extensive experience in backend development and software engineering wil
l be invaluable. His expertise will contribute to the design and implementation of robust AI-driven solutio
ns, enhancing the program's technological capabilities.

"
Aaron Blackman,https://www.linkedin.com/in/aaron-blackman/,Startup mentoring,"Aaron Blackman is a seasoned 
entrepreneur and investor with over 18 years of experience in building and scaling capital-efficient, high-
growth B2B SaaS companies. As the Founder of Venture10x, he focuses on investing in and supporting startups
, leveraging his extensive background in creating successful ventures, including two notable exits. Previou
sly, he founded Retail Express, a pioneering omni-channel retail platform that enabled over 7,000 merchants
 to process over $60 billion in retail sales before its acquisition by Maropost. Aaron's expertise in busin
ess growth strategies, product development, and market innovation positions him as a valuable mentor in the
 Tokenizer program, where he is committed to empowering local startups and SMBs to harness the potential of
 generative AI and robotics for transformative growth."
Raeleen Kaesehagen,https://www.couriermail.com.au/news/queensland/sunshine-coast/community/this-is-me-mudpu
ttys-raeleen-kaesehagen/news-story/f99a34fac76e252e31186dc3b640a008?amp,Enterprise support,"Raeleen Kaeseha
gen is a Pearcey award-winning technology entrepreneur, startup founder, and mentor. She founded Octahedron
 Software, a retail SaaS platform, at the age of 22, scaling it to clients in 27 countries before exiting s
uccessfully (now called Swim). Raeleen now invests in, mentors, and consults to high-growth tech companies,
 sharing her deep expertise in scaling startups. As a startup mentor in the Tokenizer program, Raeleen will
 leverage her experience to guide founders through growth challenges, offering strategic insights and foste
ring innovation. Additionally, she co-curates the Tech Founders group and represents Noosa’s tech ecosystem
 on the Sunshine Coast ICT industry group."
Steve Telburn,https://www.linkedin.com/in/steve-telburn/,"Enterprise support
Venture mentor","Steve Telburn is a seasoned CEO and venture partner with extensive experience in guiding d
eep-tech startups from inception to profitability, exit, or failure, often supported by Series A funding fr
om leading Australian venture capital firms. With a background in pharmacology and psychology from Monash U
niversity, he has successfully led five startups, leveraging artificial intelligence, machine learning, and
 automation to drive revenue growth and cost reduction for clients. As a venture partner at Antler, he faci
litates the growth of emerging businesses, while his advisory roles in organizations like Exercise & Sports
 Science Australia enhance strategic planning and governance in the healthcare sector.

In addition to his entrepreneurial ventures, Steve has played a pivotal role in public funding initiatives,
 having contributed to the allocation of over $500 million in startup innovation grants across Australia. H
is leadership at Secret Sauce Technology Ventures and participation in various boards, including Industry I
nnovation and Science Australia, showcase his commitment to fostering innovation and commercialization in t
he tech ecosystem. Steve's multifaceted expertise positions him as a valuable mentor in the Tokenizer progr
am, where he will provide critical insights on navigating the challenges of generative AI and robotics, ult
imately helping local startups and SMBs unlock their potential."
Luc Pettett,https://www.linkedin.com/in/lucpettett/,Exemplar AI Founder,"Luc Pettett is a seasoned entrepre
neur and investor with a rich background in technology, venture capital, and innovation. As the Founder and
 CEO of Telescope AI, he specializes in leveraging artificial intelligence to drive transformative solution
s across various sectors. Previously, Luc led Punters.com.au, Australia's premier horse racing publishing p
latform, until its acquisition by News Corp, showcasing his capability to scale startups successfully. His
investment portfolio spans diverse industries, including therapeutics, drone reforestation, and space debri
s monitoring, underlining his commitment to impactful ventures. Luc's extensive experience in AI, capital m
arkets, and automation positions him as a valuable mentor in the Tokenizer program, where he aims to foster
 local talent and accelerate the growth of AI-driven startups and SMBs in the Sunshine Coast region."
Pip Bingemann,https://www.linkedin.com/in/pipbingemann/,Exemplar AI Founder,"Pip Bingemann is the co-founde
r of Springboards.ai, an innovative suite of AI tools designed to enhance and accelerate creativity for age
ncies. With a robust background in marketing and strategy, Pip has held pivotal roles in leading organizati
ons, including Head of Brand Marketing at Unstoppable Domains, where he successfully built the company's fi
rst brand strategy, resulting in a significant increase in brand distinctiveness and a 5x revenue growth. H
is previous experience at Cutwater saw him developing new agency offerings that generated about 50% of the
agency's profit, while his strategic insights led to multiple award-winning campaigns during his tenure at
Bohemia Group. Pip's extensive expertise in artificial intelligence, creative strategy, and brand positioni
ng will be invaluable to the Tokenizer program, where he aims to inspire local startups and SMBs to harness
 the transformative power of AI."
Andrew Birt,https://www.linkedin.com/in/andrewbirt/,Exemplar AI Founder,"Andrew Birt is a seasoned tech ent
repreneur and founder based in Sunshine Coast, Queensland, with a robust background in building innovative
companies. As the founder of HubSpoke and UpSure, he has successfully spearheaded ventures that integrate m
odern insurance solutions with advanced technology, particularly in the realms of embedded insurance and ge
nerative AI. Notably, Andrew co-founded LIFX, a leading smart lighting brand that sold over 2 million units
 and achieved a $15 million Series A funding before its acquisition in 2019, followed by a second acquisiti
on in 2022.

With a strong focus on entrepreneurship and strategic development, Andrew has played a pivotal role in nurt
uring over 200 clients through UpSure, a dedicated insurance broker for the tech sector. His extensive expe
rience in startups, product development, and marketing, alongside his recognition as a winner of the Visa E
verywhere Initiative in 2018, positions him as a valuable contributor to the Tokenizer program. His mentors
hip will be instrumental in guiding local startups and SMBs as they navigate the transformative landscape o
f AI and robotics."
Dale Rankine,https://www.linkedin.com/in/dalerankine/,"Exemplar AI Founder
Startup mentor","Dale Rankine is a seasoned entrepreneur and innovator based on the Sunshine Coast, Queensl
and, with extensive experience in building, scaling, and exiting ventures across a diverse range of industr
ies, particularly in technology and digital solutions. As the founder and former CEO of Reekoh, an Industri
al Integration Cloud platform that was acquired by Autodesk, Dale has demonstrated a keen ability to bridge
 the physical and digital worlds, enhancing operational efficiencies through innovative software solutions.
 He is currently the Founder of Cogenuity, a private venture studio focused on developing profit-led ventur
es, and co-founder of multiple startups leveraging AI technologies, including UtiliSight and Vaire.

Dale's strategic insights and hands-on experience in technology commercialization, coupled with his role as
 Entrepreneur in Residence at UQ Ventures, position him as a vital mentor for the Tokenizer program. His co
mmitment to fostering local talent and supporting startups aligns perfectly with the program’s objectives t
o upskill and empower businesses in generative AI and robotics, ensuring they are well-equipped to navigate
 the evolving landscape of digital transformation."
Kris Owens,https://www.linkedin.com/in/krisowens/,Exemplar AI Founder,"Kris Owens is a dynamic co-founder a
nd executive recruiter with extensive experience in the staffing and technology sectors. Currently the Co-F
ounder of NextPlay and the Director of Business Development at Imminently, Kris leads initiatives to enhanc
e hiring experiences and drive business growth through innovative AI solutions. His previous role as Partne
r and Head of Product at nDeva resulted in record-breaking client placements and revenue, showcasing his st
rong track record in talent management and business development. Additionally, as the host of the ""Startup
 to Summit Series"" podcast, he engages industry leaders in discussions that illuminate the intersection of
 technology and recruitment. With a commitment to fostering local talent and driving innovation, Kris is po
ised to make significant contributions to the Tokenizer program, helping startups and SMBs leverage AI tech
nologies for transformative success."
Oscar Lloyd,https://www.linkedin.com/in/oscar-lloyd-a84b83272/,Technical support,"Oscar Lloyd is a passiona
te mechatronics and physics student at The University of Queensland, specializing in robotics and AI. As th
e Founder of ProxiTech, he develops innovative AI and robotics applications for the manufacturing and servi
ce sectors, while also offering educational services in collaboration with organizations such as the Peregi
an Digital Hub and RoboCoast. Oscar has led and executed complex projects, including AI-powered robotic sys
tems, and is recognized for his critical thinking and collaborative skills.

His accolades include winning first place at the UQMARS Microcontroller Hackathon and the UQMARS Arduino Ha
ckathon, along with being a recipient of the prestigious UQ Academic Excellence Scholarship. Oscar's commit
ment to the Tokenizer program will be instrumental in mentoring emerging startups and SMBs in embracing AI
and robotics solutions, fostering innovation, and enhancing the local tech ecosystem."
Noah Moller,https://www.linkedin.com/in/noah-moller/,Youth program,"Noah Moller is the CEO and Founder of T
etrix, a budding software company based in Australia, specializing in innovative solutions for the tech ind
ustry. With a background in digital leadership at Noosa Council, Noah is poised to make significant contrib
utions to the Tokenizer program. His expertise in software development extends across various programming l
anguages, including Swift and Python, showcasing his versatility in the tech landscape.

Noah's commitment to fostering skills in generative AI and automation aligns perfectly with the goals of th
e Tokenizer program, as he is dedicated to empowering startups and small businesses to leverage cutting-edg
e technologies. By mentoring participants and sharing his insights on practical applications of AI, Noah ai
ms to drive innovation and economic growth within the Sunshine Coast region. His leadership and vision will
 be instrumental in nurturing local talent and building a collaborative tech community."
Craig Manson,https://www.linkedin.com/in/craig-manson/,Venture mentor,"Craig Manson is a seasoned Chair, No
n-Executive Director, and Advisor based in Noosa Heads, Queensland, with extensive experience in leading bu
sinesses across technology, banking, financial services, and consumer goods sectors. He has a proven track
record of fostering sustainable growth through strategic execution, organizational transformations, and coa
ching high-performing teams. His leadership roles include serving as Director at Manson & Co., where he adv
ises on business performance and innovation, and as a Non-Executive Director at various firms, including Al
ex Bank and PurchasePlus, focusing on governance and strategic oversight.

Craig's expertise in driving change and leveraging technology positions him as a vital mentor for the Token
izer program. He excels in cultivating collaborative environments that encourage diverse thinking and rigor
ous discussions, making him instrumental in guiding startups and SMBs to embrace AI-driven solutions and in
novations. His profound understanding of business dynamics and commitment to fostering growth will signific
antly enhance the program's mission to transform the Noosa region’s tech landscape."
Rob Easton,https://www.linkedin.com/in/robert-easton-a4260311/,Angel mentor,"Robert Easton is an accomplish
ed Chief Financial Officer and founder with over 20 years of experience in financial management, strategy d
evelopment, and organizational transformation. Currently serving as the CFO & Founder of CFOPRO in Brisbane
, he has successfully guided medium to large organizations through complex financial landscapes, including
navigating the challenges posed by the Global Financial Crisis and COVID-19. His extensive expertise in fin
ancial reporting, strategic planning, and cash flow management has contributed to substantial sustainable g
rowth across various sectors, including accounting, software, and health care.

In addition to his corporate roles, Robert has made significant contributions as a mentor, supporting busin
ess growth initiatives for startups and small businesses through programs like River City Labs and the Quee
nsland Government's ACE program. His commitment to fostering innovation and financial acumen aligns perfect
ly with the goals of the Tokenizer program, where he will provide invaluable insights and mentorship to eme
rging companies seeking to leverage generative AI and automation technologies for their growth and success.
"
Vinko Grgic,https://www.linkedin.com/in/vinkogrgic/,Angel mentor,"Vinko Grgić is an accomplished Operations
 and Product Leader based on the Sunshine Coast, Queensland, with over a decade of experience driving growt
h for startups and scale-ups. He has a proven track record in building teams and systems that foster succes
s, having taken a VC-backed startup from inception to IPO. Vinko's analytical prowess combined with his peo
ple-focused approach allows him to implement customer-obsessed cultures that drive tangible commercial outc
omes. His current roles include Operations Lead at Aussie Angels, where he enhances support for the Austral
ian startup ecosystem, and as an LP at Co Ventures, Australia's first dedicated pre-seed venture fund, wher
e he identifies and nurtures ambitious founders. Vinko's expertise in strategy, mentorship, and operational
 management positions him as a vital contributor to the Tokenizer program, driving innovation and supportin
g local startups in their AI journeys."
Coby Sullivan,https://www.linkedin.com/in/cobysullivan/,Startup mentor,"Coby Sullivan is a seasoned marketi
ng and community engagement expert with a robust background in entrepreneurship, innovation, and journalism
. Currently, Coby serves as the Marketing & Community lead at Sprint Ventures, where she focuses on investi
ng in critical sectors such as AI and health. Her previous role as Head of Founder Communities at Innovatio
n Bay saw her build a thriving network of over 80 tech founders across Australia and New Zealand, fostering
 collaboration from seed to Series C stages. Coby's experience includes facilitating MIT coursework for the
 Australian Health Accelerator, where she mentored top founders in honing their investment readiness.With a
 strong focus on strategy, community building, and digital marketing, Coby brings invaluable expertise to t
he Tokenizer program. Her commitment to supporting startups and small businesses aligns perfectly with the
program's goals of enhancing local economic growth and innovation in AI. Coby's unique blend of skills posi
tions her as a crucial mentor, empowering the next generation of entrepreneurs in the Sunshine Coast region
."
Kyle McManus,https://www.linkedin.com/in/kcmcmanus/,Sales & BD Mentor,"Kyle McManus is the Director at Saga
n Consulting, where he specializes in providing strategic guidance to high-growth technology companies thro
ughout Australia and New Zealand. With over 25 years of experience in the technology sector, Kyle has held
leadership roles at prominent firms including Sitecore and Objective Corporation, where he drove significan
t revenue growth and established market strategies. His expertise in enterprise software, sales management,
 and leadership development has empowered numerous startups to enhance their sales processes and operationa
l efficiencies.

Under his direction, Sagan Consulting has become a vital resource for technology companies seeking to navig
ate the complexities of sales and leadership in a rapidly evolving market. Kyle's commitment to innovation
and mentorship aligns seamlessly with the goals of the Tokenizer program, where he aims to foster local tal
ent and drive the adoption of AI and automation solutions among startups and SMBs in the Noosa region."
Mark Edwards,https://www.linkedin.com/in/mark-edwards-consultant/,Sales & BD Mentor,"Mark Edwards is a seas
oned consultant and the Founder of Remarkable Results, specializing in business development and sales trans
formation for enterprise-level organizations across the public and private sectors. With an extensive backg
round in strategic change leadership, Mark has successfully implemented tailored solutions that enhance ope
rational efficiency and foster high-performance cultures. His notable projects include leading a transforma
tional sales capability initiative for Telstra, impacting over 600 sales professionals, and driving a 30% i
ncrease in seller confidence. Mark’s commitment to continuous learning is evident through his recent AI Fou
ndations for Business specialization with IBM, positioning him to effectively guide startups and SMBs in le
veraging AI and automation. As a mentor in the Tokenizer program, Mark will contribute his expertise in bui
lding resilient leadership teams and navigating industry disruptions, driving meaningful change in the Suns
hine Coast tech ecosystem."
Cliff Benns,https://www.linkedin.com/in/cliff-benns/,Automation Mentor,"Cliff Benns is a seasoned entrepren
eur and business mentor based in Noosa Heads, Queensland, with over 26 years of experience in founding and
leading multiple multi-million dollar enterprises. As the Founder and CEO of Sustainable Food Corporation a
nd Sustainable Food at Home, Cliff is committed to addressing critical global challenges such as food waste
 and soil degradation through innovative, zero-waste solutions. His previous ventures, including Total Cool
ant Management Solutions and Direct Mining & Industrial International, showcase his ability to identify mar
ket needs and develop sustainable products, earning him a reputation as a leader in environmental stewardsh
ip.

In his role as a Business Mentor at Purpose Driven Business Coaching, Cliff empowers entrepreneurs and busi
ness owners to transform their ventures into purpose-driven enterprises that make a positive impact on soci
ety and the environment. He is passionate about fostering an entrepreneurial ecosystem that prioritizes sus
tainability and innovation, making him a valuable asset to the Tokenizer program. Cliff's extensive knowled
ge in AI applications, coaching, and business strategy positions him to guide startups toward adopting gene
rative technologies and solutions that drive efficiency and growth."
Kieran Browne,https://kieranbrowne.com/bio/,Tech Mentor,"Kieran Browne is tech lead with Springboards.ai, a
 startup building AI tools for creative agencies. He is a creative technologist, researcher and occasional
artist
Kieran Browne has a background in visual arts and a PhD in machine learning. His laurels include several pe
er-reviewed publications, an artwork exhibited at the National Gallery of Australia, and being briefly cite
d in the French wikipedia article on artificial intelligence. His creative practice is primarily software b
ased but incorporates elements of old media. Amongst his works are drawing machines, generative art, an ant
i-surveillance camera app, and a ouija board that can compute neural networks."
Test User yczkhjxs,https://example.com/user-yczkhjxs,Test Mentor,This is a test user created on 20250301_20
4321 to verify sync functionality. The user has a random identifier yczkhjxs to ensure uniqueness. This ent
ry should be synced to the Google Drive spreadsheet.
Test User c614c541,https://example.com/user-c614c541,Test Mentor,This is a test user created on c614c541. T
his should appear in Google Drive after sync.
Bob Jones,https://example.com/user-c614c522,Bobby Mentor,This is a test entry by cb

```

---

_****_





Now I can see what's happening. The script is working correctly in terms of:
1. Finding the knowledge base directory
2. Reading the manifests
3. Selecting relevant documents
4. Accessing the files

However, there seems to be an issue with the content selection. Looking at Steve Ringo's bio from the Bios.csv file:

```
Steven Ringo is a seasoned technology executive, currently serving as the Vice President of IT & Security at Epiminder, a leading biotechnology firm focused on developing innovative EEG recorders for epilepsy monitoring. With a strong foundation in electrical engineering and an MSc in Engineering Management from the University of the Witwatersrand, Steven brings over two decades of diverse experience in software architecture, cloud solutions, and AI-driven technologies. He has successfully led transformative projects at prestigious organizations, including Amazon Web Services, where he guided software businesses in modernizing their applications and adopting cloud solutions. Throughout his career, Steven has been instrumental in architecting scalable systems and implementing best practices in cloud computing, particularly within regulated environments like healthcare. As a mentor in the Tokenizer program, he will leverage his extensive expertise in AI and software development to empower startups and SMBs in the Sunshine Coast region, fostering innovation and driving economic growth. His commitment to upskilling local talent and enhancing technological capabilities aligns perfectly with the program's vision, making him a valuable asset to the Tokenizer initiative.
```

The issue is that the script is working as designed, but the content selection model might need some tuning. Let me make a few suggestions for improvement:

1. The LLM's selection of documents could be improved by:
   - Adding more context about the specific use case (writing a bio for a talk)
   - Adding weights or relevance scores to the selected content
   - Filtering out test documents and irrelevant content

2. The knowledge base creation could be improved by:
   - Better formatting of CSV content into markdown tables
   - Adding headers and sections to make the content more readable
   - Filtering out test entries and empty rows

Would you like me to modify the script to make these improvements? Or would you prefer to use the existing content to write the bio for Steve Ringo's upcoming talk on AI agents?

---



---

