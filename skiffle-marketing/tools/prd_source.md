# PRD [v1.2]

# Skiffle Rebuild (Mobile-First Native App), Product Requirements Document

## Stakeholder overview

**Right now.** We are reviewing this plan with stakeholders before the build begins. Ryan is working on tickets and clarity on feature assessment. We are also trying to figure out best way to keep the marketing website in sync.

**Project in plain terms.** We are rebuilding the Skiffle dealer app as a true mobile app for iPhone and Android, replacing today's version that was built for desktop and only stretched onto a phone. The first release does what the current app already does, minus one visual styling tool, so dealers get a faster, native experience they can trust in front of a client.

**Where we are in the process.** The plan is essentially settled. What the first version includes, how we will measure success, and the rough launch window (before the January shows) are decided. A small number of choices are still open and are marked for discussion below.

**What is next.** Iron out some collaboration tools and clean up the plan, begin the build (next week), and show working prototypes at the first demo in August, aiming to launch in early December.

## Contents

* Stakeholder overview
* v1 scope

1. Overview
2. Problem statement
3. Goals and non-goals
4. Success metrics
5. Target users
6. User stories and use cases
7. Requirements
8. Scope
9. Assumptions and dependencies
10. Design and UX
11. Milestones and timeline
12. Risks and open questions
13. Explicitly deferred to v2 and beyond
14. Preliminary ideas from brainstorming
15. Appendix
16. Go-to-market and launch
17. Stakeholder FAQs
18. Images
19. API and data model
20. QA and testing
21. v2 vision
22. Competitor review
23. Open notes

|||
|  ---  |  ---  |
|**Author**|Ryan Stephen (PM), Niki Beck (Tech Lead), Latham Nance (Business Lead)|
|**Stakeholders**|Tyler D. Franklin, Christian Smith, Mark, Wen, Lauren|
|**Target release**|v1 (Late December 2026)|
|**Build target**|Replit, React Native, Expo (EAS Build plus OTA)|


## **How to read the status tags**

|Tag|What it means|
|  ---  |  ---  |
|**[LOCKED]**|Confirmed, not being reopened|
|**[DECIDED]**|Chosen in this planning round, pending final confirmation at the PRD review|
|**[TENTATIVE]**|Provisionally set but flagged for further discussion, may change|
|**[NEEDS DISCUSSION]**|Flagged as a topic for the review, the current entry is the working recommendation|
|**[OPEN]**|A real decision still to make|
|**[CANDIDATE]**|A nice-to-have for v1 or under consideration for v2, still needs definition|
|**[V2+]**|Deliberately deferred beyond v1|
|**[PRELIMINARY]**|An idea from brainstorming, captured for consideration, not committed|
|**[WATCH]**|Locked, but carries execution risk to monitor|
|**[FIX]**|A verified defect in today's app to resolve in v1|
|**[VERIFIED]**|Confirmed by the live-app crawl (Boozer McClure account)|


---

## v1 scope

v1 is basic parity with the current app, with two deltas. The StyleFlow dynamic visualizer (the editor) is excluded, and the Shoulder Slope is a nice-to-have rather than a requirement. Beyond parity, three things are genuinely new in v1, the Dashboard (likely a minimal landing page, widgets TBD), the app showing the dealer's own logo instead of Trinity's (FR-34), and a simple manual todo list (FR-35). Navigation is five bottom tabs: Dashboard, Orders, Clients, Fabrics, and Resources. The foundation under all of it (sign-in on existing Trinity credentials, both platforms from one codebase, Rails as the data source, and the store-update-plus-forced-update launch) is assumed.

**Dashboard (new, likely minimal in v1)**

* Dealer Rank widget, the rank pill (moved here from Orders) with a tap-through to the full Rank Report.
* Global search, using the same constraints, UX, and data as the web app.
* An order-status summary showing the roll-up counts (Pending, In Progress, Delayed). Tapping a status opens the Orders tab pre-filtered to that status.
* Estimated ship dates and any further widgets are TBD.

**Orders**

* A table of orders, with search and filters (by status, by client, and so on).
* An Order details page for each order. Viewing is native. Editing an order is not built in-app, it links out to WorkFlow (FR-31).

**Fabrics**

* Search, filter, camera scan of a folder QR code, and voice input on fabric search (FR-32).
* Collection pages and individual fabric pages with today's functionality (favorites and so on).
* Fabric notifications, the full management surface, view the subscriptions list, edit a subscription, and unsubscribe all, not just a passive alert (FR-33).
* Download of the fabric swatch and garment images, and related-fabric suggestions.
* The dynamic garment render is view-only. The StyleFlow editor is excluded.

**Clients and Resources**

* Clients, the client list with an A-to-Z index and the client profile with order history, read-only measurements, contact actions, notes, photos, and the Cloud Closet (view garments, delete, and archive) (detailed in the requirements section).
* Resources, tutorials, the materials pack view, spec charts, and other reference content. The full list is TBD.

**Nice-to-have and not in v1**

* Nice-to-have, the Shoulder Slope flagship. Wanted for v1 and the shows, but not required, and the first thing to cut if the build runs hot.
* Not in v1, the StyleFlow editor (dynamic visualizer), biometric sign-in, fabric OCR, custom linings, custom model creation, style pages, an in-app password reset, order creation, and payments.

## 1. Overview

Skiffle today is a desktop web app in a mobile wrapper, responsive enough to view on a phone but designed top-down for desktop. The v1 rebuild is a ground-up, mobile-first native app built on React Native and Expo, shipping on iOS and Android from a single codebase. Its job is to faithfully rebuild the existing information architecture and feature set ("parity") while spending a small "native dividend" on the handful of experiences native genuinely unlocks. v1 is deliberately the foundation, the proven native base the broader roadmap (ordering, measurements, customization, insights) gets built on later.

The parity baseline is defined by the current live app, cross-checked against the team's user stories and the crawl notes. Where the crawl found a defect, v1 fixes it rather than faithfully reproducing it (see sections 7 and 12).

## 2. Problem statement

The limitation is architectural, not cosmetic. A desktop app made viewable on mobile cannot be polished into a mobile-first app, it has to be rebuilt as one. Because the current app isn't native, whole classes of in-the-field dealer experience can't even be considered.

The single strongest rebuild argument from the crawl is the Measurements seam. Reaching measurements today kicks the dealer out to external Safari and demands a second Workflow login, mid-fitting, in front of a client. That one flow captures why the wrapper is the problem and why native is the answer.

Evidence it's worth doing now. The install base is about 60 dealers (roughly 32 on Android plus a similar iOS count), while blended daily active use sits in the high teens and Android stickiness averages about 16 percent, both jumpy and not climbing. Dealers dip in to check one thing rather than living in the app. The digitized baseline is in section 4.

## 3. Goals and non-goals

**Goals**

* Rebuild Skiffle as a mobile-first native app, bottom-up for the phone. 
* Establish the native, mobile-first foundation the whole roadmap can build on. 
* Ship iOS and Android at v1 from one React Native and Expo codebase. 
* Achieve feature and IA parity with today's app, plus the native dividend. 
* Drive adoption, dealers reaching for the app in mobile moments.

**Non-goals**

* No ground-up redesign of features and flows. Structure and behavior are the spec.
* No order creation, payments, offline, or measurement write path in v1. Editing an existing order is not built natively either, it links out to WorkFlow (FR-31).

## 4. Success metrics

We measure adoption, and we hold one cross-platform definition so iOS and Android are finally comparable. The figures below are a first digitized baseline (see the caveats at the end of this section).

**North Star, primary .** Adoption, meaning a sustained lift in daily active use and stickiness, trending up on a single standardized cross-platform metric put in place at launch. The truest signal is a dealer reaching for the app in a mobile moment rather than waiting for desktop.

**Standardized metric definition .** Today the two stores report different things, which is exactly why the numbers below don't line up. Standardize on two figures computed identically on both platforms:

* Daily active devices as an absolute count (the base is small, so absolute beats percentages, one dealer is about 3 percent).
* Stickiness as a trailing-30-day DAU over MAU ratio.

Capture the current readings as the documented "before," which is what this section now records. Implement this in Amplitude, one product-analytics tool across both platforms, with a single SDK, identical event definitions, and product metrics like retention and funnels out of the box. The store dashboards (App Store Connect, Play Console) stay as install-base references only, not the source of truth.

**Baseline snapshot, digitized from the current app metrics (Mar to Jun 2026).**

|Platform|Metric as tracked today|Window observed|Typical value|Range|Read|
|  ---  |  ---  |  ---  |  ---  |  ---  |  ---  |
|iOS|Active devices per day|31 Mar to 5 May, plus 22 to 28 Jun (middle of the window not captured)|about 12 per day (10.6 in late June)|3 to 22|Low teens, flat to slightly declining, last reading 3|
|Android|Installed audience|31 Mar to 7 May|about 32|28 to 36|Install base essentially flat|
|Android|Stickiness (DAU/MAU, labeled "daily")|31 Mar to 7 May|about 16 percent|4 to 41 percent|Highly volatile, no upward trend|
|Blended|Approximate daily active users|derived|high teens (iOS active about 12 plus Android DAU about 5)||Low-to-high teens, jumpy, not climbing|


This is the quantified "why now." Usage is small, erratic, and not growing, and the two platforms currently cannot be compared because they track different things. Full daily data is in the companion file `skiffle-usage-baseline.csv`.

**Secondary signals.** The flagship is trusted in front of clients, the app ships continuously via OTA, and dealers are glad to open it (sentiment).

**Targets (v1).** From the baseline, the working v1 targets are a blended daily-active lift from the high teens to about 30 within 60 days of launch, and a trailing-30-day stickiness floor of about 25 percent within 90 days. These are the thresholds to confirm at the review. Because the base is about 60 dealers, always pair any ratio with the absolute count and with direct dealer conversation so a single dealer doesn't swing the read.

**Guardrails.** Neither platform should regress while the other grows, and OTA update adoption should stay healthy.

**Caveats on the baseline.**

* The figures are transcribed from photographs of a printout, so verify them against the source analytics export before circulating.
* The iOS series is missing 6 May to 21 June, so the iOS trend is indicative, not complete.
* Android's ratio is labeled "daily," so confirm whether it is a same-day DAU over MAU or a trailing-window ratio, since that changes how stickiness reads.
* Blank Android days (2, 5, 10, and 26 April) are gaps or zero-activity days and are treated as missing.

## 5. Target users

Three dealer archetypes. v1 optimizes for Frank first, utterly reliable, dead simple, never embarrassing, while still serving Dale and Sal.

* **Frank, the Veteran (low-tech), center of gravity.** Wants order status or a fabric instantly during a client call. His core is order status plus search, flawless and simple.
* **Dale, the Closer.** Sells on the move with the model library, collections, fabrics, new client (with photos), and a shoulder-slope reading. His core is model library, find fabric, new client, and the flagship.
* **Sal, the Boutique Owner.** Tracks each order's production stage, catches delays early, and keeps client records sharp. Her core is tracking depth, carrier visibility, and notifications.

Sub-account staff (an associate working for an owner like Sal) are already in scope because sub-account permission gating is a v1 requirement (see FR-3).

The throughline is that order status plus search is the non-negotiable core all three depend on.

## 6. User stories and use cases

* As any dealer, I open the app and land where the state of my business is immediately visible, with my orders one tap away.
* As Frank, I look up an order's status or a fabric instantly during a client call.
* As Dale, I browse the model library, collections, and fabrics and capture a new client (with photos) on the move.
* As Dale, I take a shoulder-slope reading with my phone and record it in my own process.
* As Sal, I see per-garment production stage plus inline carrier tracking and get notified of delays and shipments.
* As any dealer, I run one global search across clients, fabrics, orders, and item numbers, scoped to my permissions.

The board maps these to a full story set (OLD-01 to OLD-32 for current behavior, US-01 to US-32 for targets), which is the detailed source for acceptance criteria.

## 7. Requirements

### Functional requirements

|ID|Requirement|Status|Notes|
|  ---  |  ---  |  ---  |  ---  |
|FR-1|Authentication via Replit OAuth, linked to Trinity credentials|DECIDED|Replit OAuth is the sign-in flow, but it validates against Trinity's native credentials through Trinity APIs, so dealers sign in with the same identity they already use on the web. There is no separate app login and no new password. The exact Replit-to-Trinity credential link is still being finalized with the tech team. Supersedes the earlier separate-login plan|
|FR-2|Store the session and tokens in a hardware-backed secure store (expo-secure-store, iOS Keychain and Android Keystore)|LOCKED|Not plain AsyncStorage. The Replit OAuth flow manages the session established over Trinity credentials|
|FR-29|Replit-to-Trinity credential and session bridge|DECIDED|The Replit OAuth flow validates against Trinity credentials via Trinity APIs, and the authenticated session authorizes Rails data calls scoped to that dealer. Because the identity is the dealer's existing Trinity account, there is no separate account, no first-run account creation, and no new-account friction at the cutover|
|FR-3|Server-driven, API-enforced permissions, app renders nav and features from credentials|LOCKED|Price-list gating for sub-accounts is in scope. Hiding UI is presentation only, the API is the real gate. Permissions key off the dealer's Trinity account, the same identity used to sign in (FR-1)|
|FR-4|Shoulder Slope flagship, live device-tilt inclinometer via expo-sensors, large degree readout; include user preference toggle to reverse the active shoulder orientation so that dealer can stand front or back of client|CANDIDATE, v1 nice-to-have|Not camera or CV. Display-only, the app does not persist the value. Error state is an instrument guard, not data validation. Wanted for v1 and the January-shows story, but a nice-to-have rather than a requirement, and the first thing to cut if the build runs hot|
|FR-5|Measurements, native read-only view|LOCKED|Replaces today's Safari plus second-Workflow-login kickout. Action, confirm the Rails measurements read path exists|
|FR-6|View orders, order to its garments to each garment's production stage|LOCKED|Status is per-garment, not one order-level badge|
|FR-7|Full production pipeline ported at parity, display-only from Rails|LOCKED|Fabric Hold through Delivery, plus Direct Ship and Cancelled. Home keeps the simplified Pending, In Progress, Delayed roll-up. Submitted orders only|
|FR-8|Inline carrier tracking, Rails proxies the carrier API with keys server-side|LOCKED, revised|Multi-carrier (UPS, FedEx, or DHL), not UPS only. The estimated shipping delivery (ESD) date, latest status, last scan or location, and tracking number are shown inline. The ESD date is tappable and deep-links to that carrier's tracking page with the tracking number prefilled and progress shown. This revises the original "dealer never taps out" stance: primary tracking stays inline, and the carrier site is an optional tap for full history|
|FR-9|Global search, server-side via Rails, debounced predictive, permission-scoped|LOCKED|Resolves five entity types, Fabric ID, Fabric Collection, Client, Order ID, and Garment ID. A bare Garment ID must resolve distinctly from an Order ID, and a Collection name distinctly from a single fabric. Must accept an item number as `T2-1881370`, `t2 1881370`, or bare `1881370` (prefix normalization). See FIX-5 for the two-index defect|
|FR-10|QR scan-to-find for fabric folders, resolves via global lookup, opens fabric detail|LOCKED|Reuses the flagship's camera stack. See FIX-6 for dead legacy codes|
|FR-11|Writes (read-mostly v1), create and edit client plus contacts, upload photos to a client, add a photo to a garment, delete and archive a garment in Cloud Closet, favorite fabrics per dealer|LOCKED|Photo upload at two attach points. The garment photo, delete, and archive are the writes into the otherwise read-only order domain. Delete and archive need a confirm-guard and Rails endpoints (see the API section)|
|FR-12|Resources hub for v1, tutorials, the materials (Digital Materials Pack) view, spec charts, and other reference content still to be finalized (candidates include the model library, options library, fitting guide, and the permission-gated fabric price list)|LOCKED|Fabric Explorer is now its own Fabrics tab, not under Resources. Dropped, Embroidery (Template and Text), not in production. The hub is named Resources (FR-17)|
|FR-13|Push notifications, transactional order-lifecycle for delayed, shipped, and delivered, plus chat-reply push|DECIDED|Delivered through the native OS push channels directly, APNs on iOS and FCM on Android, coded per platform, with no Intercom or third-party push provider. The delayed alert is the highest-value one. Rails emits an order-status event and the app registers a device token (see the API and data model section). Include an opt-in and preferences step tied to Account and Settings. Intercom stays scoped to live chat (FR-27), never transactional push|
|FR-14|Client text notes ("Add Notes")|DECIDED, writable in v1|Joins the small write set alongside FR-11, per-dealer and per-client. Needs a Rails notes write endpoint|
|FR-15|Account and Dealer Profile, and where Account and Logout live|DECIDED, view-only in v1|Account is reached from a persistent avatar icon in the top-right of every tab, opening the Account and Profile screen and Logout. This is the home for Account and Logout in the five-tab nav. Profile fields are not editable in v1. The one functional exception is the push opt-in (FR-13), handled by the OS permission prompt plus a simple on/off since there is no profile write path. Granular per-event push preferences and profile editing are deferred. Password recovery is manual via support (FR-19). The web My Account is captured in a later pass (per Latham)|
|FR-16|Reference content (spec charts, fitting and materials guide, price list, and so on) served remotely from Rails or a CMS so updates don't need an app release|DECIDED, remote-updatable|Today all of it is live web content, so remote is both parity and correct. Hardcoding would be a regression|
|FR-17|Reference-hub naming|DECIDED, "Resources"|The reference hub is a bottom-nav tab named Resources (section 10), holding tutorials, the materials pack, spec charts, and other reference content (the full list is TBD)|
|FR-18|Dealer Rank pill plus Rank Report (new to this doc, a parity feature)|LOCKED (parity), one FIX|Rank pill or widget on the Dashboard opens a full report covering MTD and YTD, rank among neighbors, and multi-year history. A second entry sits in Resources. FIX-1, on the 1st of the month the pill reads "N/A" with a red minus-100-percent arrow (MTD reset), v1 must fall back to YTD or a trend, never "N/A"|
|FR-19|Password recovery|DECIDED, no in-app flow in v1|No in-app forgot-password flow in v1. Recovery stays manual as it works today, the dealer contacts support and support resets the password. A self-serve flow is a future improvement. Keeping it manual is what lets v1 authenticate against existing Trinity credentials without extra build. Apply Now (FR-20) is separate and unaffected|
|FR-20|Apply Now destination (new)|DECIDED|Points to [https://trinity-apparel.com/get-started](https://trinity-apparel.com/get-started) in a web-view, replacing today's Trinity 404|
|FR-21|Client-list navigation for roughly 1,280 clients|DECIDED, A-to-Z index|An alphabetical jump-to-letter index over the client list, with global search still available. Replaces today's single endless scroll|
|FR-22|Per-client order history|VERIFIED parity|The client profile already has an inline Orders section with per-garment badges, it is the per-client aggregation v1 wants. Ports as-is, correcting an earlier assumption that it was missing|
|FR-23|Options (Image and Info) and View Fabric Status|DECIDED, folded into fabric detail|Both fold into the fabric detail screen rather than living as separate entry points. Content is retained, the clunky separate entries go away|
|FR-24|Client Insights, query by Ordered or Not-Ordered, garment type, and date range for windowed counts|V2+, removed from v1|The hidden long-press entry on the Clients tab is removed for v1, so the feature is not reachable in v1. The full revamp is deferred to v2 pending a definition of the job it solves|
|FR-27|Intercom live chat, an in-app support messenger|DECIDED, v1|A persistent in-app chat so a dealer can reach support without leaving the app or emailing, reached from the Resources tab and surfaceable contextually. This is the in-app chat that the FR-13 chat-reply push points to. Uses the Intercom React Native SDK. Engagement-grade latency is acceptable here, which is why Intercom serves chat while transactional push stays on the native OS channels (FR-13)|
|FR-28|Client contact actions on a client profile|DECIDED, v1|Tap to call, tap to email, and tap to map using the device's native handlers (tel, mailto, maps), shown when the client record holds the matching contact data. Restores the 2022 design's contact affordances|
|FR-30|First-run onboarding|DECIDED, v1|A short first-run walkthrough of the non-negotiable features (sign-in, finding an order, search, clients, and fabrics with the garment render), aimed at the low-tech veteran who only adopts if the first run is hand-held. Intro cards plus a few contextual tooltips, skippable and re-openable from Resources|
|FR-31|Edit Order, link-out to WorkFlow|DECIDED, v1|Editing an existing order is not built natively. Where a status allows an edit, the app links out to WorkFlow (web), matching how it works today. WorkFlow is not mobile-optimized, so this is a deliberate fallback for the rare must-do case, not a primary flow. Native order editing is deferred (section 13). Order creation stays out entirely (section 3)|
|FR-32|Voice input on fabric search|DECIDED, v1|The Find-a-Fabric search keeps its native microphone, speech-to-text into the query, porting today's behavior. Voice is scoped to fabric search only. Global search and client search stay text, since they have no mic today, so this is not a regression there|
|FR-33|Fabric notifications management|DECIDED, v1|Port the full notifications apparatus, the subscriptions list, editing a subscription (the Edit Modal), Unsubscribe All, and the email and notes fields, not just a passive out-of-stock alert. The APIs already exist in the system, so this is wiring the native UI to them. This covers FIX-4, a favorite that goes unavailable surfaces here rather than silently|
|FR-34|White-label dealer logo|DECIDED, v1|The dealer's logo already lives in Trinity's system, so it is pulled on sign-in (via the Trinity credentials, FR-1, returned by `GET /me`) and shown in the app in place of Trinity's branding. No uploader or picker in v1. Display constraints, a fixed header slot with a max height and width and preserved aspect ratio, and a fallback to Trinity branding when a dealer has no logo on file. This is a deliberate carve-out from the single standardized design (section 10), the logo is the only per-dealer element, while colors and theme stay standardized. An image uploader is v2 (v2 vision)|
|FR-35|Simple todo list|DECIDED, v1|Manual, user-generated todos a dealer can create, edit, archive, and delete. Freeform text, not linked to a client or order in v1, and not a with-the-client tool since dealers have little time in a meeting. Needs a new Trinity table so the same todos can surface on the web later. The v2 direction is action-based todos generated from events (v2 vision)|


### Verified defects to resolve in v1 (`FIX`)

|ID|Defect (verified in the live app)|Resolution direction|
|  ---  |  ---  |  ---  |
|FIX-1|Rank pill shows "N/A" and minus 100 percent on the 1st (MTD reset)|Fall back to YTD or a trend, never "N/A" (see FR-18)|
|FIX-2|Client Edit, Delete sits beside Save, red, with no confirmation, and can wipe years of history|Add a confirm-guard. Backend clarify, hard versus soft delete, blocked when orders exist|
|FIX-3|Cloud Closet hides garments older than 3 years by default|Default to all-time, or explicitly show that a filter is applied|
|FIX-4|A favorited fabric can go Not Available silently|Resolved, surfaced through the ported fabric notifications management (FR-33) rather than a manual status-table check|
|FIX-5|Two search indexes, the Fabrics tab shows current V26 collections while home search only matches roughly 2023-era ones|Unify search scope and index (relevant to FR-9)|
|FIX-6|Older physical fabric-folder QR codes are dead links (the scanner itself works)|Ops dependency, who fixes or redirects the printed folder codes. Confirm what a scan resolves to, fabric detail versus collection|
|FIX-7|Delayed view, the All, Open, Completed radios silently disappear, and no delay reason is shown|Restore filter visibility. Surfacing a reason needs Rails to expose one, see backend items|
|FIX-8|Polish debt, an "Edit Client Client" page title, Options Library node overlap, and a wrong breadcrumb at the choice-card level|Fix in the rebuild, don't port the overlapping node layout blindly|


### Non-functional requirements

* **Connectivity.** Online only. No offline cache, sync, queued writes, or conflict resolution in v1.
* **System of record.** The existing Rails API called directly. No BFF, add a thin shim only if a concrete need appears.
* **Performance.** Raw native performance is part of the native dividend.
* **Shipping.** EAS Build plus OTA updates.
* **Design system.** Standardized, light and dark following the system setting, token-based. The one per-dealer element is the dealer's own logo (FR-34), otherwise no per-dealer theming or customization.
* **Garment render (must-have).** The Fabric Explorer garment render, a dynamic Picario image keyed by fabric, garment type, and model, with the swatch and garment toggle, is the emotional selling moment, dealers screenshot it into client texts. It is served as a dynamic URL (the fabric is in the URL), so the app composes the URL and shows the image, no proxy needed. Handle a missing or failed render gracefully by falling back to the swatch. A confirmed v1 must-have.

## 8. Scope

**In scope, parity-plus**

* IA, screens, content, and flows matching what exists today (parity), defined against the live app.
* The native dividend, meaning the measurement and camera flagship, push, and raw performance.

**Out of scope**

* Everything in the deferred list (section 13). Offline was explicitly considered and cut.

## 9. Assumptions and dependencies

Assumptions to validate, each becoming a backend work item wherever it isn't true today:

* Rails can expose everything v1 needs, meaning global search across the four domains, per-garment order status, the permission model, photo-upload endpoints, and a carrier-proxy endpoint (UPS, FedEx, DHL).
* JWT auth is available from Rails, and carrier developer keys (UPS, FedEx, DHL) exist for the server-side proxy.
* Content-driven reference screens can be served from a remote source.

Backend items surfaced by the crawl:

* Rails must emit order-status events on state change, the shared dependency under every push option, scope it first.
* Identity bridge, define how a Replit-authenticated session authorizes Rails data calls, and build the mapping from a Replit login to its Trinity dealer record and permissions (FR-29). Without it the app cannot scope data or enforce access.
* A delay reason likely doesn't exist in the data today, confirm whether Rails can expose one (FIX-7).
* Client delete semantics need definition (hard or soft, order-blocked) before the guard is designed (FIX-2).
* Sub-account behavior is largely unverified. Each unknown (what a sub-account sees, price-list gating, and so on) is one login-as-sub-account check away, and each answer becomes an API requirement for the data model and ERD.

## 10. Design and UX

* **Visual direction.** The old design file is the previous design, not the target. The visual layer is an open exploration (Mobbin-driven) while IA, screens, and flows hold at parity.
    * **SIDE QUEST:** Explore expanded Trinity branding so that all documents, digital platforms, and marketing is consistent. Potential for a brand refresh. **ETA: Aug 12 for discussion.**
* **Navigation.** A five-item bottom navigation: Dashboard, Orders, Clients, Fabrics, and Resources. Resources is the reference hub (tutorials, materials pack, spec charts, and more, FR-17). This supersedes the earlier four-tab More-and-Tools structure.
* **Account and Logout.** A persistent avatar icon in the top-right of every tab opens the Account and Profile screen and Logout (FR-15). It stays reachable from any tab, matching today's app, and is the home for Account and Logout now that More is gone.
* **Home and landing.** The app opens on the Dashboard, which is also a bottom-nav tab. In v1 it is a minimal landing page, the rank widget, global search, and an order-status summary whose statuses tap through to a filtered Orders list (see v1 scope). Orders stay one tap away so the dashboard does not bury them.
* **Design system.** Standardized, light and dark (system setting), token-based. The one per-dealer element is the dealer's own logo, which replaces Trinity's branding in the header (FR-34). Everything else stays standardized, with no per-dealer theming.
* **Component library.** Use gluestack-ui, a universal React Native component kit, for the frontend UI. It fits the token-based design system and gives the team prebuilt components to move quickly. This supersedes the earlier NativeWind recommendation.

## 11. Milestones and timeline

**Team and roles (from the kickoff canvas).** Named leads are Ryan Stephen (Project Manager), Niki Beck (Tech Lead), and Latham Nance (Business Lead). Listed stakeholders are Tyler D. Franklin, Christian Smith, Mark, and Wen. Kickoff attendees were Niki, Latham, Tyler, Christian, and Ryan.

Ownership:

* Backend and API, the critical path, is owned by Niki (Tech Lead), with Christian supporting front-end.
* Design is a shared team responsibility, developed in conjunction with AI-assisted exploration (Mobbin-driven), rather than a single named design lead.
* Still to confirm: QA and release ownership.

Proposed schedule, back-planned from a launch before the January 2027 industry shows, which are the anchor since each show season is a window to debut a production launch and keep the hype up. These dates are tentative because building with AI can compress traditional timelines in ways we cannot yet predict, and this launch is itself an experiment to learn how AI-assisted delivery plays out so we can forecast future projects more accurately.

|Milestone|Date|Notes|
|  ---  |  ---  |  ---  |
|Kickoff grilling and alignment session|29 to 30 Jun 2026|Completed|
|Pre-PRD alignment doc|17 Jul 2026|Completed|
|PRD review with stakeholders|29 Jul 2026|Approval gate. Includes pre-marketing site and video|
|Leadership Update|12 Aug 2026|WIP update; prototype was available but too early to really dive into; [Monday.com](http://Monday.com) research precedence.|
|Demo Day 1 (prototypes)|End Aug (TBD; add to calendar)|Casual presentation of current prototype|
|Demo Day 2 (prototypes)|TBD|TBD|
|Feature-complete build, internal alpha begins|Late Sep 2026|AI-assisted build may reach this sooner|
|QA and hardening, Android sensor validation, backend endpoints integrated|Early-to-mid Oct 2026|Less compressible than build|
|Beta to TMCs (TestFlight and Play closed testing)|Late Oct 2026|The 5 to 8 TMCs, per the GTM plan|
|Beta feedback in, code freeze, store submission|Mid Nov 2026|Published as an update to the existing listings|
|Store approvals, staged rollout, dealer comms and training ready|Late Nov 2026||
|Go/no-go, full launch, forced-update gate flips|Early Dec 2026|iOS and Android together, before the January shows|
|Industry shows, debut|Jan 2027|The anchor driving the schedule, not a build milestone|


**Critical path and timeline risks.**

* Backend readiness is the true critical path, not the app. Rails order-status events, the carrier proxy (UPS, FedEx, DHL), the measurements read path, a delay reason, the identity bridge (FR-29), and the permission and sub-account model all need an owner and a schedule now, in parallel with design, or they will gate the launch. The API and data model section is the first-cut contract to build from.
* Store submission and rollout gate the date. Apple and Google review plus a staged rollout need a buffer before the full-launch milestone, which means a code freeze and submission ahead of it, with store assets, privacy and data-safety disclosures, and a beta (TestFlight and Play testing) sequenced earlier still.
* The window from Demo Day 2 to full launch has to absorb hardening, QA, the Android sensor validation (section 12), beta feedback, store review, and dealer change-management, so build should be well underway before Demo Day 2. The AI-assisted build may free up time here, which the team should treat as buffer rather than a reason to pull the non-compressible gates forward.
* The push notification path is now decided (native APNs and FCM, section 12), leaving the carrier proxy and the identity bridge as the biggest backend items to sequence early.

## 12. Risks and open questions

|Risk or question|Status|Notes and next step|
|  ---  |  ---  |  ---  |
|Push notification delivery path|DECIDED|Native OS push, APNs on iOS and FCM on Android, coded per platform, no Intercom or third-party provider (FR-13). Rails emits order-status events and the app registers a device token|
|RN component library choice|DECIDED|gluestack-ui (section 10)|
|Home, dashboard versus orders-landing balance|DECIDED|Dashboard first, with orders one tap away and order state surfaced so orders aren't buried (section 10)|
|Client-list navigation for roughly 1,280 clients|DECIDED|A-to-Z index (FR-21)|
|Order-list pagination|DECIDED|Progressive load (infinite scroll), fetching about 50 to 100 per batch, with filters and search to narrow. The list remembers its position and active filters when the user leaves and returns|
|Reference-hub naming|DECIDED|Named Resources, a bottom-nav tab (FR-17)|
|Account and Logout placement|DECIDED|Persistent top-right avatar on every tab, opening Account, Profile, and Logout (FR-15, section 10)|
|Edit Order|DECIDED|Not native in v1, links out to WorkFlow where status allows (FR-31)|
|Cloud Closet garment delete and archive|DECIDED, v1|Added to the write set (FR-11), behind a confirm-guard, with Rails endpoints to build|
|Fabric notifications management|DECIDED, v1|Port the full apparatus, the list, per-item edit and Edit Modal, Unsubscribe All, and email and notes (FR-33). APIs already exist. Covers FIX-4|
|Fabric search voice input|DECIDED, v1|Keep the native mic on fabric search (FR-32). Global and client search stay text, no regression|
|Client notes writable; profile editable|DECIDED|Notes writable in v1 (FR-14); profile view-only in v1 (FR-15)|
|Reference content remote versus baked in|DECIDED|Remote-updatable via Rails or CMS in v1 (FR-16)|
|Options and View Fabric Status fold-in|DECIDED|Folded into fabric detail (FR-23)|
|Client Insights entry in v1|DECIDED|Removed for v1, revamp stays v2 (FR-24)|
|Client-profile contact actions (call, email, map)|DECIDED, v1|Restored using native handlers, shown when contact data exists (FR-28)|
|Auth and identity|DECIDED|Replit OAuth as the sign-in flow, validating against Trinity's native credentials so dealers use their existing web identity (FR-1). The session bridge authorizes Rails calls (FR-29). No separate login and no new-account friction at cutover. No in-app password recovery in v1, recovery stays manual via support (FR-19)|
|Analytics standardization across iOS and Android|DECIDED|Amplitude, one tool across both platforms, with one shared definition (absolute daily active devices plus trailing-30-day stickiness). Store dashboards stay as install-base references only. Confirm what Android's "daily" DAU/MAU actually measures|
|Custom Linings scope|OPEN, v2|Nice-to-have, not v1, detailed in the v2 vision section. When picked up, scope the Rails endpoint that replaces the JotForm and confirm the write-set expansion|
|Custom Models viewer and editor|OPEN, v2, needs research|Nice-to-have, not v1, detailed in the v2 vision section. When picked up, split the lighter grid viewer from the heavier line-drawing editor|
|Android sensor accuracy for Shoulder Slope|WATCH|Validate on a representative set of Android phones before launch|
|"Two truths," shipment is order-level while status is garment-level|WATCH|The UI must hold both, and the granular to roll-up mapping lives in Rails|
|ESD (Estimated Shipping Delivery) behavior|DECIDED|Sourced from the carrier API and shown inline. Tapping the date deep-links to the carrier's tracking page (UPS, FedEx, or DHL) with the tracking number prefilled and progress shown. Pre-ship, ESD may be a factory estimate, labeled as such (the "ESD - Factory" source). See FR-8|


## 13. Explicitly deferred to v2 and beyond

Conscious deferrals, not omissions:

* Order creation and submission, the single biggest deferred item, ordering stays in WorkFlow web. Native order editing is deferred too, the app links out to WorkFlow for edits (FR-31).
* Payments, offline, editing measurements and shoulder-slope save, dealer theming, per-fabric OCR, full carrier scan history and live map, and biometric auth. Token refresh is now handled by Replit OAuth (FR-2), so it is no longer a deferred item.
* Unified identity, single sign-on across the app and WorkFlow, once WorkFlow is rebuilt. v1 already signs in with the dealer's existing Trinity credentials (FR-1), so there is no separate login, only the unified SSO across both products is deferred.
* Client Insights revamp, cut pending a definition of the job it solves.
* Custom Models and Custom Linings. Nice-to-haves, not v1, detailed in the v2 vision section.

## 14. Preliminary ideas from brainstorming

These come from the Skiffle Kickoff brainstorming board and are captured as preliminary, not committed. Where one conflicts with a LOCKED call, the current PRD wins and the idea is noted as a divergence to reconcile.

**Dashboard and home concept** The brainstorm reframes the Orders landing as a light dashboard. Ideas raised:

* A Dealer Rank chip at top-left showing rank only, with no dollar amounts (an explicit dealer request), a trend arrow versus last month, and a tap-through to the Rank Report (US-03, US-04, US-05).
* A headline announcement banner that is dismissable (US-08, US-09).
* At-a-glance business state, meaning order status, number of clients, and delays or notifications.
* A Delays tab carrying a red badge with the count of late orders (US-12).
* Order-list controls, meaning an All, Open, Completed filter, a sort dropdown, pagination at about 100 per page, and collapsible order cards (US-13, US-14, US-15, US-17).
* A Saved tab for work started but not submitted (US-11), which only becomes meaningful once order creation exists (v2).

The dashboard's actual contents are still the open question from section 10. This is the menu of candidates, not a locked layout.

**Navigation model** Two different structures appear on the board and need reconciling:

* A persistent top navigation with Orders, Clients, Fabrics, University, Support, Marketing, and My Account (US-01), which introduces University, Support, and Marketing as new areas.
* A four-item bottom nav of Orders, Clients, Fabrics, and More (from the in-depth app-flow walkthrough), with everything else under More.

Resolved. v1 uses a five-item bottom nav (Dashboard, Orders, Clients, Fabrics, Resources), with the reference hub named Resources (section 10). The top-nav areas Support and Marketing are not v1, and University is folded into Resources.

**Intercom live chat** US-31 proposes a persistent in-app live-chat messenger so a dealer can get immediate support on an order or platform question without leaving the app or sending an email. It fits the responsive human backstop that the closer archetype relies on. Resolved. This is now a v1 feature, FR-27, using Intercom for chat, reached from the Resources tab. Transactional push stays on the native OS channels (FR-13), so Intercom is scoped to chat only.

**Onboarding** An App Launch flow proposes onboarding with intro cards plus contextual tooltips, aimed at the low-tech veteran who will only adopt if the first run is hand-held. Resolved. Included in v1 as a short first-run walkthrough of the non-negotiable features (FR-30).

**Account menu** A richer account menu is sketched, covering profile edits, push preferences, an App Guide, and log out, replacing today's avatar, name, and log-out-only screen. This overlaps FR-15 (profile editing) and the FR-13 opt-in step, and it gives push preferences somewhere to live.

**Export all orders** US-30 proposes an Export All Orders button that downloads a CSV, so a dealer can analyze history in a spreadsheet or share it. A new read and export path, no write.

**Biometric and Face ID [PRELIMINARY, diverges from a v2 deferral]** The Auth Standalone flow floats Face ID setup and extracting Forgot Password into its own flow. Face ID conflicts with the current deferral of biometric auth to v2. The Forgot Password extraction aligns with FR-19. Kept preliminary, biometric stays v2 unless reprioritized.

**Flow-design backlog** The board carries a priority list of flows still to be designed, useful for sequencing design work:

* High, the Clients flow (list, detail, images, measurements, cloud closet, communication) and a New Order Creation flow focused on custom models.
* Medium, My Account and Settings, and Tools or University (Model Library, Options Library, Rank Report, and Shoulder Slope sub-flows).
* Low, Auth standalone (extract Forgot Password, add Face ID setup).

The High-priority "New Order Creation flow focused on custom models" reflects the brainstorm's enthusiasm, but the current decision keeps both order creation and custom models out of v1 (section 13). The design work can still be sequenced, it just targets v2.

**Order grouping, a superseded idea** US-16 proposes grouping orders under a client-name header. This is superseded by the locked decision to show one card per Dealer Order with client names repeating (FR-22 context and the flow-archaeology ruling). Recorded here only so the brainstorm story isn't lost.

## 15. Appendix

* **Primary source.** The Skiffle Rebuild, Pre-PRD Alignment (Trinity Apparel kickoff session).
* **Evidence base.** The flow-archaeology board, one flowchart per tool, OLD versus NEW, with a live-app crawl (Boozer McClure account) plus reconciliation against Niki's design files (2022, 2024, and 2026 eras). Each flow carries a crawl-confidence percentage and a manual-checks list of open verifications. Findings are point-in-time, newest wins. "Clothier" and "dealer" are used interchangeably.
* **Story sets.** OLD-01 to OLD-32 (current behavior) and US-01 to US-32 (targets) are the detailed acceptance-criteria source.
* **Brainstorming source.** The Skiffle Kickoff board (product-development canvas, the US-01 to US-32 story wall, in-depth Orders and Fabrics flow walkthroughs, component and reference-library inventories, and the flow-design backlog). Section 14 draws from it. Ideas there are preliminary and predate the locked decisions elsewhere in this doc.
* **Usage baseline.** `skiffle-usage-baseline.csv`, digitized from photographs of the current iOS (Active Devices) and Android (DAU/MAU and Installed audience) printouts covering March to June 2026. Section 4 summarizes it. Transcribed from images, so verify against the source export.

## 16. Go-to-market and launch

### Strategy

This is a migration and adoption launch to a known base of about 60 dealers, not an acquisition launch. Success is defined in section 4, adoption measured as daily active use and stickiness against the baseline. GTM is led by Lauren (marketing and communications) with Latham (Business Lead).

### Positioning and messaging

First-pass value proposition by persona, to confirm and sharpen.

|Persona|Key pain today|How the app solves it|Proof point|
|  ---  |  ---  |  ---  |  ---  |
|Frank, the veteran|Fumbling in front of a client, cannot pull up order status or a fabric fast enough|Instant, dead-simple order status and search in his pocket|Dashboard-first home with orders one tap away, global search, one-tap order lookup|
|Dale, the closer|Friction on the move that breaks the pitch|His whole showroom and tools on his phone|Model library, find-fabric, new-client capture with photos, and the shoulder-slope flagship|
|Sal, the boutique owner|Surprise delays and losing track of production|Per-garment production visibility and proactive alerts|Per-garment status, inline carrier tracking with ESD, and delayed, shipped, and delivered push|


### Roll-out phases

* Phase 1, internal alpha. Smoke test and critical bugs, internal team, via TestFlight and Play internal testing.
* Phase 2, private beta. Validate core value and train the TMCs as the launch enablement layer. Internal plus about 5 to 8 TMCs, via TestFlight and Play closed testing.
* Phase 3, full launch. All dealers, forced update, old version retired (see cutover below). Dates are in section 11.

### Launch tier and channels

Tier 1, a coordinated push. Channels are an email announcement, an in-app notice and banner, rep and TMC 1:1 outreach, a Webflow news article, and an Intercom announcement.

### Enablement

* Dealer training, an in-app onboarding tour, a Help Center with FAQs, and short how-to videos.
* TMC enablement, the TMCs are trained first in beta and act as the 1:1 human layer that walks low-tech dealers through the cutover.
* Support, the Help Center, Intercom live chat (FR-27), and TMC coverage.

### Cutover and migration

* Approach, publish the new app as an update to the existing store listings, so existing installs auto-update from old to new.
* Same-identity requirement, the same Apple bundle ID and the same Android package name and signing key, or the stores treat it as a new app with no auto-update. Confirm the accounts and keys with the Tech Lead. This is the single biggest gotcha.
* Backstop, a minimum-version gate forces the stragglers onto the new version and retires the old one.
* Sign-in, dealers use their existing Trinity credentials (FR-1), so there is no new account, they simply sign back in. Recovery stays manual via support (FR-19).
* No grace period, the gate flips at full launch, so the update must be live and propagated in both stores and sign-in must work before it flips.

### App store submission

* iOS, TestFlight for alpha and beta, then App Store review, with privacy nutrition labels prepared. Android, Play internal and closed testing, then production, with the Data safety form completed.
* Publish as an update to the existing listings, not a new app.
* Staged rollout, plus EAS OTA for fast fixes after launch. Code freeze and submission around mid-November (section 11).

### Go, no-go, and rollback

* Go criteria to finalize: the beta bug bar cleared, Android sensor validation passed, the required backend endpoints live, the TMCs trained, and both store approvals in hand.
* Rollback, hold the min-version gate so the old version keeps working, ship fixes over OTA, and flip the gate only once full launch is stable.

### GTM risks

* A forced cutover on an older, mixed-tech base. Mitigate with TMC 1:1s, in-app onboarding, and pre-launch comms.
* Store review delays the date. Submit early with a buffer and use the staged rollout.
* A sign-in wall at cutover. Some dealers will have forgotten their password, so staff support for a spike in manual resets.

## 17. Stakeholder FAQs

**Executive / business alignment**

1. What is the real business outcome of v1?
2. What adoption target would make this rebuild “worth it”?
3. Are we comfortable shipping a parity-first app, rather than using the rebuild to rethink workflows?
4. What must be ready before the January shows?
5. What are we willing to cut if the timeline gets tight?
6. What is the stakeholder decision needed today versus later?

### Scope and prioritization

1. What exactly counts as parity?
2. Which features are truly non-negotiable for v1?
3. Are Custom Models and Custom Linings definitely out of v1?
4. Why is order creation excluded?
5. Is the dashboard too much for v1, or is it essential to adoption?

**Dealer / user experience**

1. Will low-tech dealers understand the new app immediately?
2. Do we need onboarding in v1?
3. What is the first-run experience?
4. How do we avoid embarrassing the dealer in front of a client?
5. What are the highest-value mobile moments?
6. How will sub-account staff experience the app?

**Product analytics and success measurement**

1. Which analytics tool are we choosing: PostHog, Amplitude, or something else?
2. What events define “active use”?
3. What is the v1 adoption target and time window?
4. How will we measure quality of adoption, not just opens?
5. How will we compare iOS and Android consistently?

**Design and navigation**

1. Is the five-tab navigation final (Dashboard, Orders, Clients, Fabrics, Resources)?
2. What lives on the dashboard at launch?
3. How prominent should Dealer Rank be?
4. What is the visual target?

**Operations, support, and rollout**

1. How will dealers be trained or introduced to the new app?
2. Will this replace the existing app listing or launch as a new app?
3. Will dealers be forced to update?
4. Who owns support once this ships?
5. What happens to the current app during transition?

## 18. Images

::: {.layout}
::: {.column}
![image.png](https://trinityapparel.slack.com/files/U099WNJ6946/F0BLSUQMMD2/image.png)
:::
:::

::: {.layout}
::: {.column}
![image.png](https://trinityapparel.slack.com/files/U099WNJ6946/F0BLL08JX8V/image.png)
:::
:::

::: {.layout}
::: {.column}
![image.png](https://trinityapparel.slack.com/files/U099WNJ6946/F0BLL0FEUFP/image.png)
:::
:::

::: {.layout}
::: {.column}
![image.png](https://trinityapparel.slack.com/files/U099WNJ6946/F0BLH1MES67/image.png)
:::
:::

## 19. API and data model (draft)

This is a first cut to get the backend moving, not a final contract. The app talks to the existing Rails API directly, so most of v1 is confirming or exposing what Rails already has, plus a small number of new endpoints. Since the app itself is vibe-coded on Replit, treat the endpoint list as the target the generated client codes against, and let the exact request and response shapes settle as the build proves them out.

### Conventions worth setting up front

Replit will scaffold most of this by default. The ones worth being deliberate about:

* REST over HTTPS, JSON payloads, a versioned base path such as `/api/v1`.
* A bearer token (the authenticated session from FR-1 and FR-29) on every request, stored in expo-secure-store, never in plain storage.
* Every list and record scoped to the dealer from the token on the server. Never trust a dealer id sent by the client.
* Cursor-based pagination on all list endpoints, returning a next cursor, so the client can remember position and infinite-scroll.
* A single consistent error shape so the app handles failures uniformly.
* All secrets (carrier API keys, APNs and FCM keys) stay server-side only.

### Endpoints v1 needs

Status column: New means build it, Confirm means it likely exists in Rails and just needs verifying or exposing.

**Identity and account**

|Endpoint|Purpose|Status|
|  ---  |  ---  |  ---  |
|`POST /auth/session`|Exchange the Replit OAuth result for a Trinity-scoped session, the identity bridge (FR-29)|New|
|`GET /me`|Current dealer, profile, permissions, and logo URL, drives nav, gating, and the white-label logo (FR-3, FR-34)|Confirm|
|`POST /devices`|Register a device push token, platform and token, for notifications (FR-13)|New|
|`DELETE /devices/{id}`|Unregister a device on logout or opt-out|New|


**Search**

|Endpoint|Purpose|Status|
|  ---  |  ---  |  ---  |
|`GET /search?q=`|Global search resolving five entity types, Fabric ID, Fabric Collection, Client, Order ID, and Garment ID, permission-scoped, with item-number prefix normalization (FR-9). A bare Garment ID resolves distinctly from an Order ID, and a Collection name distinctly from a single fabric. Unify the two indexes (FIX-5)|Confirm and unify|


**Orders**

|Endpoint|Purpose|Status|
|  ---  |  ---  |  ---  |
|`GET /orders?status=&client_id=&cursor=`|Paginated order list with status and client filters (FR-6)|Confirm|
|`GET /orders/{id}`|Order detail down to each garment's production stage (FR-6, FR-7)|Confirm|
|`GET /orders/{id}/tracking`|Carrier tracking and ESD through a server-side proxy, UPS, FedEx, DHL (FR-8)|New (proxy)|
|Order-status events|Rails emits an event on each state change so a push can fire (FR-13). A delay reason exposed here if it exists (FIX-7)|New|


**Clients**

|Endpoint|Purpose|Status|
|  ---  |  ---  |  ---  |
|`GET /clients?letter=&cursor=`|Client list feeding the A-to-Z index (FR-21)|Confirm|
|`GET /clients/{id}`|Client profile with order history (FR-22) and contact fields (FR-28)|Confirm|
|`POST /clients`, `PATCH /clients/{id}`|Create and edit a client and contacts (FR-11). Define delete semantics, hard or soft, blocked when orders exist (FIX-2)|Confirm and define|
|`GET /clients/{id}/measurements`|Read-only measurements, replacing the Safari kickout (FR-5)|Confirm read path|
|`POST /clients/{id}/notes`|Write a client note (FR-14)|New|
|`POST /clients/{id}/photos`, `POST /garments/{id}/photos`|Photo upload at the two attach points (FR-11)|New or confirm|
|`DELETE /garments/{id}`, `POST /garments/{id}/archive`|Delete or archive a garment in Cloud Closet (FR-11), behind a confirm-guard|New|


**Fabrics**

|Endpoint|Purpose|Status|
|  ---  |  ---  |  ---  |
|`GET /fabrics?q=&filter=&cursor=`|Fabric search and filter|Confirm|
|`GET /fabrics/{id}`|Fabric detail, favorite state, availability, related fabrics|Confirm|
|`GET /collections/{id}`|Collection page|Confirm|
|`POST /fabrics/{id}/favorite`, `DELETE /fabrics/{id}/favorite`|Per-dealer favorite toggle (FR-11)|Confirm|
|`GET /fabrics/resolve?code=`|Resolve a folder QR code to a fabric or collection (FR-10, FIX-6)|New or confirm|
|`GET /fabrics/notifications`, `PATCH /fabrics/notifications/{id}`, `DELETE /fabrics/notifications`|Fabric notification subscriptions, list, edit one, and unsubscribe all (FR-33, FIX-4). APIs already exist in the system|Confirm|


The garment render itself needs no endpoint, the app composes the Picario image URL from the fabric (see section 7).

**Rank and reference**

|Endpoint|Purpose|Status|
|  ---  |  ---  |  ---  |
|`GET /rank`|Dealer rank data, MTD, YTD, rank among neighbors, and trend, with the fallback so it never returns N/A on the 1st (FR-18, FIX-1)|Confirm|
|`GET /resources`|Remote-updatable reference content, tutorials, materials pack, spec charts (FR-16)|New or CMS|


**Todos**

|Endpoint|Purpose|Status|
|  ---  |  ---  |  ---  |
|`GET /todos`, `POST /todos`, `PATCH /todos/{id}`, `DELETE /todos/{id}`|Simple user-generated todos, list, create, edit, archive (via a status), and delete (FR-35). A new Trinity table so the same todos can surface on the web later|New|


### Data model to pin down

* The identity bridge, how a Replit identity maps to a Trinity dealer record, its permissions, and any sub-accounts. Sub-account behavior (what they see, price-list gating) is still unverified, and each answer becomes a rule here (FR-3).
* Order to garments to per-garment status, holding the two truths, shipment is order-level while production status is per-garment.
* Client delete semantics (FIX-2) and whether a delay reason exists (FIX-7).

## 20. QA and testing

The build is AI-assisted and will move fast, which makes testing the guardrail rather than an afterthought. Generated code gets checked against the parity baseline and the acceptance criteria, not trusted because it runs.

### Layers

* Smoke checks on the critical paths (sign-in, order lookup, search, fabric detail, measurements) on every build.
* A manual QA pass using the FR and FIX lists as the checklist, run on both iOS and Android, since one codebase still behaves differently per platform.
* A device matrix of real phones, including older and low-end Android for the Frank persona and for the shoulder-slope sensor validation.
* A regression pass on the eight FIX items specifically, so fixed defects don't quietly return.

### TMC beta

The TMCs are friendly customers who double as the human enablement layer, so they test and get trained at the same time.

* Cohort, the internal team plus about 5 to 8 TMCs, on TestFlight and Play closed testing.
* Give them a short script covering the non-negotiable jobs (look up an order, run a search, open a client, show a fabric and its garment render), then let them free-play their real workflow.
* Make reporting one tap from inside the app (the Intercom chat or a feedback button), or a low-tech tester won't report at all.
* Watch Amplitude during the beta to confirm events actually fire and the funnels read before launch depends on them.
* Triage weekly, sorting each item into fix-before-launch or fast-follow over OTA.

### Bug bar and exit

* P0, anything touching sign-in, wrong or missing data, or a crash, blocks launch.
* Everything else can ship as a fast-follow given OTA.
* Go criteria, all P0s cleared, the FIX list verified, Android sensor validated, sign-in solid on both platforms, and Amplitude events confirmed. This feeds the go/no-go in section 16.

## 21. v2 vision

Features deliberately held for v2, kept here so the intent is not lost and the v1 requirements stay focused. Neither is in v1. Both were FR-25 and FR-26 in earlier drafts.

**Custom Linings**

A light native form that lets a dealer submit images for a custom-lining request, replacing the existing web JotForm. It adds a form plus image upload to the write set, with the same camera-or-library and cellular file-size handling as the v1 photo writes (FR-11), and it needs a Rails endpoint to receive submissions. When picked up, confirm the write-set expansion and the endpoint that replaces the JotForm.

**Custom Models**

Two parts. A viewer showing saved custom models in a grid, where each model is a saved collection of validated garment options, the lighter lift and the closest to surfacing the existing saved-model concept. And an editor that lets a dealer build a custom model with visual line-drawing selectors, the heavier lift that needs research. If it is pulled forward, the viewer lands before the editor.

Open items to settle when Custom Models is picked up: the naming ("Custom Models" versus "Saved Styles"), the known 10-character name-truncation bug in the existing web configurator, what a saved model actually does in the app given that order creation is also v2, and the sequencing of the grid viewer ahead of the line-drawing editor. The flow-archaeology board had shown an active push to build custom models now, but the current call keeps both out of v1.

**Logo image uploader**

v1 pulls the dealer's logo from Trinity on sign-in (FR-34). v2 adds an uploader so a dealer can upload or replace their own logo in the app, with the image constraints (format, transparent background, dimensions, aspect ratio) enforced at upload.

**Action-based todos**

The v1 todo list (FR-35) is manual and freeform. The v2 direction turns notifications into actions, todos generated automatically from events, each opening to the detail and the next step. Examples, "choose a replacement fabric for Ben's order" when a chosen fabric goes out of stock, which opens to related fabrics matching the source fabric's characteristics, "update your credit card," "send a thank-you to Ben after your meeting," and "schedule a delivery for Ben" when a garment reaches the deliver phase. This builds on things v1 already has, out-of-stock surfaces through fabric notifications and related-fabrics already exists, so the work is wiring events to todos and adding the entity links the v1 todos deliberately skip.

**Alterations tracking**

When a delivered garment needs adjustment, the dealer sends it to a local alterations shop and has no way to track it today. A v2 alterations flow would record what the alterations are, route to the shop, and track status and return, essentially a second, outward-facing production pipeline. Open questions, is the alterations shop a tracked entity, who updates status, and does it reuse the order-status UI.

**QuickBooks and Calendly integrations**

Candidates to validate, not commitments. QuickBooks for the financial and accounting side, and Calendly for scheduling client meetings, which pairs with the action-based todos ("schedule a delivery," "send a thank-you"). Both are third-party integrations that carry their own scoping.

## 22. Competitor review

A light, point-in-time scan of Trands USA (Dayang Trands), a direct made-to-measure competitor, based on their public site and clothier resource library, not a hands-on dealer-account walkthrough. External context, not a feature checklist to match.

**Their dealer platform.** Trands clothiers order and sell through USTYYLIT (currently version 4, launched January 2023), a web-based garment-design and ordering platform. It is browser-based and login-gated, the same category as Trinity's WorkFlow, and no native iOS or Android clothier app surfaced in either app store.

**What USTYYLIT does well.** Fast cart-based order entry (their pitch is ordering a jacket, trouser, and shirt in under five minutes), a dynamic wardrobing tool called STYYLcart that generates garment images on demand (their analog to our Picario garment render), a body-measurement and remote-selling mode for virtual fittings over video call, custom linings built from a dealer's own photography or artwork, and fabric swatchbooks.

**What this means for Skiffle.**

* The clearest gap in their favor is mobile. Their clothier tool is web-only, so a genuinely mobile-first native app is a real differentiator for Trinity, which is exactly Skiffle's bet.
* Several USTYYLIT strengths are things Skiffle deliberately defers, fast order entry (order creation is v2), custom linings (v2 vision), and deeper measurement tooling (v1 is read-only). On ordering depth they are ahead, and that is a conscious v1 tradeoff, not an oversight.
* Their dynamic garment images confirm the garment render is table stakes in this category, not a novelty, which supports keeping it a v1 must-have.

This is a surface read from public materials. A dealer-account walkthrough of USTYYLIT would sharpen it, and it should be refreshed periodically since their platform updates regularly.

## 23. Open notes

Captured observations that are not yet decisions and do not drive scope on their own.

**Usage during active selling (stakeholder note).** A stakeholder observed that dealers likely will not lean on the app much during active selling, they have little time in a client meeting. Part of this is habit, the old Trinity software was clunky and not always white-labelled, so dealers avoided pulling it out in front of clients. This suggests the app's real value sits in preparation and follow-up rather than the live selling moment. To act on it, we need a phased pre-sell, sell, and post-sell use-case segmentation, so we can isolate where each feature is most useful. Recorded as a note, not a driver, nothing else in this PRD is rewritten around it yet.

# 24. Project Expenses

This section is for visibility for stakeholders and leadership to see what products or services we have started using for this project, why, the cost, and if they are scaleable in the future or limited to this project.

|Product/Service|Use Case|Plan, Cost, and Time|
|  ---  |  ---  |  ---  |
|[Replit](https://replit.com/)|AI vibe-coding platform that combines a code editor, an AI agent, a database, hosting, and deployment in a single tab, with no local installation or infrastructure setup.|Skiffle Team (3)<br>$20/mo. + additional usage|
|[Mobbin](https://mobbin.com/)|A vast collection of visual videos, and images of popular apps for inspiration and guidance. Helps fill in gaps in design and UX for the team. MCP connected to Figma. |Team Plan (2)<br>$144/quarter (only alt to annual)|
|[Monday](http://Monday.com)|Project management, communication, documentation, etc.|Initially Skiffle IC team (3)<br>$74/mo. (monthly)|
|[Amplitude](https://amplitude.com/)|User analytics for app & web (scalable)|TBD|
