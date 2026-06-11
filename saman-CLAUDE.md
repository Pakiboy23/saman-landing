# CLAUDE.md — Saman Pantry

## What this is

Saman Pantry is a pantry and provisions tracking app rooted in Pakistani and South Asian household culture. "Saman" (سامان) is Urdu for "provisions." Built for homes where staying stocked matters. Not a generic grocery app, not inventory management software, not a food blog companion.

**Parent company:** Saman Technologies LLC
**Domain:** samanpantry.com
**Bundle ID:** com.samanpantry.Saman
**Supabase project:** saman-pantry (`mcknboqvblbonmaebmjg`, us-east-1)

---

## Stack

- **Platform:** iOS 17+ (native)
- **UI:** SwiftUI
- **Data:** SwiftData (local persistence)
- **Backend:** Supabase (auth, sync, remote storage)
- **Monetization:** RevenueCat (pending integration) + Instacart IDP (pending approval)
- **Pricing:** Cosmetic-only freemium, $4.99/month or $39.99/year

---

## Project state

- App built and QA'd
- Auth trigger on Supabase creates 3 default pantries on signup
- Pending before launch: app icon, RevenueCat integration, real device testing, Instacart IDP approval

---

## Architecture

### Data model
SwiftData for local persistence. Supabase for auth and cloud sync. The app should work offline-first — local data is the source of truth, sync is additive.

### Auth
Standard Supabase Auth with real emails (unlike H.I.M.'s synthetic email model). On signup, a database trigger creates 3 default pantries for the new user.

### Monetization path
- **RevenueCat** for subscription management (StoreKit 2 under the hood)
- **Instacart IDP** for grocery ordering integration — this is the correct path. Direct store logins violate Instacart ToS.

---

## Design system

### Tokens
```
Background:    #FAF6EF   (cream)
Accent:        #C67E2A   (amber)
```

### Typography
- Primary: Cormorant Garamond
- Urdu accent text: Noto Nastaliq Urdu

### Logo
Three pantry jars mark. Primary amber jar on dark background (#1C0F00). "Saman" in Cormorant Garamond bold. Urdu accent سامان in amber (#C67E2A). Tagline: "Your kitchen, always stocked."

### Visual direction
- Clean, practical, warm
- Utility first
- Cultural grounding is present but not performative — the South Asian context is real, not decoration
- Do not make it look like enterprise software
- Do not make it look like a food blog
- Do not erase the South Asian identity

---

## Code conventions

- Swift strict concurrency where applicable
- SwiftUI declarative patterns — no UIKit unless absolutely necessary
- SwiftData for persistence (not Core Data, not raw SQLite)
- Prefer `@Observable` / `@State` / `@Environment` over older property wrappers where iOS 17+ allows
- Keep views small and composable
- No force unwraps in production code

---

## Supabase conventions

- Project region: us-east-1
- Auth trigger creates default pantries — do not duplicate this logic client-side
- Migrations must use `YYYYMMDDHHmmss` filename format
- If applying SQL directly (not through the migration CLI), register with `supabase migration repair --status applied [name]`

---

## What not to do

- Do not treat this as a generic inventory app. The cultural specificity is the product.
- Do not use enterprise UX patterns (data grids, bulk operations UI, admin panels)
- Do not introduce UIKit unless SwiftUI genuinely cannot do something
- Do not add frameworks or heavy dependencies without clear justification
- Do not use generic startup language in copy ("revolutionize", "game-changing", "seamless", etc.)
- Do not flatten the South Asian context into generic "multicultural" language
- Do not mix Saman Pantry voice/design with H.I.M. — these are completely separate products

---

## Testing

- Real device testing required before launch (TestFlight)
- RevenueCat sandbox testing for subscription flows
- Verify the 3-default-pantries auth trigger fires correctly on new signups
- Test offline behavior — app must remain functional without network

---

## Brand voice (for any copy work)

Practical, calm, warm, useful, culturally grounded. Write like someone who actually runs a South Asian household, not like someone describing one from the outside. Achievement-forward and milestone-driven for marketing copy — not salesy.

Tagline: "Your kitchen, always stocked."
