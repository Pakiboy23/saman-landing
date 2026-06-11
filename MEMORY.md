# Project Memory
Last updated: 2026-06-11 | Session 4 | Branch: main
Memory health: 9/10

## Project Overview
Saman Pantry — iOS 17+ native app (SwiftUI + SwiftData + Supabase) repositioned from barcode-scan pantry tracker to **family recipe capture product**. Core loop: capture a parent's spoken recipe (paste) → structure it without flattening vague measurements → push ingredients to shopping list → cook → pantry depletes → restock. Marketing landing page at `index.html`. Pre-launch, RevenueCat integrated, App Store submission this week.

## Where We Left Off
- **Session 4 work is complete.** Path C was chosen and executed.
- **Next immediate step:**
  1. Open Xcode → clean build (⇧⌘K) → build (⌘B) — verify zero compiler errors
  2. Run on real device or simulator — test the Recipes tab end-to-end: paste a transcript → Extract → review ingredients → Add to Shopping List → verify list appears in Lists tab
  3. Check the extraction on a REAL family transcript (the harness used authored fixtures — test with an actual phone-call recording transcript)
  4. Complete remaining ASC/RC dashboard tasks (from Session 3) if not already done
  5. TestFlight build

## What Was Built — Session 4 (Path C: Recipe Capture MVP)

### New files
| File | Purpose |
|------|---------|
| `Saman/Core/Models/Recipe.swift` | SwiftData model — title, rawTranscript, createdAt, isDirty |
| `Saman/Core/Services/RecipeExtractionService.swift` | Anthropic API (claude-sonnet-4-6) + ExtractedIngredient/Recipe structs. Exact port of extraction.py prompt and 3-rule system |
| `Saman/Features/Recipes/RecipesView.swift` | Recipes tab — Urdu empty state, recipe list, + CTA to capture |
| `Saman/Features/Recipes/RecipeCaptureView.swift` | Full capture sheet: paste → extract → review w/ toggles → add to shopping list → done state |

### Modified files
| File | Change |
|------|--------|
| `Saman/Core/Services/Config.swift` | Added `anthropicAPIKey` |
| `Saman/Core/Persistence/ModelContainer+Setup.swift` | Added `Recipe.self` to both shared + preview schemas |
| `Saman/App/RootView.swift` | Replaced Reorder tab with Recipes tab (`fork.knife` icon) |

### Key design decisions (Session 4)
- Reorder tab replaced (not removed from code, just from tab shell) — it was orphaned by the reposition
- No voice capture this version — paste-only, voice later
- No persistent ingredient sub-model — extracted ingredients go straight to ShoppingListItems (Product + ShoppingListItem)
- Recipe model stores only title + rawTranscript — no extracted JSON stored; re-extraction if needed later
- Vague amounts (null) get quantity=1 rounded up, unit from extraction or "unit"
- Anthropic key embedded in Config.swift — MUST move to Supabase Edge Function before scaling

### Extraction quality
- Harness ran 2026-06-11 against claude-sonnet-4-5: **5/5 fixtures passed, 0 invented numbers, 46/46 phrases preserved, 31/31 code-switch mappings**
- App uses claude-sonnet-4-6 (same prompt, expected same or better results)
- CAVEAT: harness fixtures are authored — test on a real family phone-call transcript before betting

## Active Work
- [ ] Xcode build + real device test of recipe capture flow
- [ ] Test on a real (non-authored) recipe transcript
- [ ] ASC: Saman Pro Yearly ($39.99/yr) — localization + price
- [ ] ASC: Saman Pro Monthly ($4.99/mo)
- [ ] ASC: Saman Pro Lifetime — Non-Consumable IAP ($79.99)
- [ ] RC: Attach real ASC products (replace Test Store placeholders)
- [ ] Xcode Cloud env vars: SUPABASE_URL + SUPABASE_ANON_KEY
- [ ] TestFlight build + real-device testing
- [ ] Move Anthropic key to Supabase Edge Function (pre-scale, not pre-submission)

## Architecture Notes
- RC configured in SamanApp.init(); user ID synced via onChange → purchases.setAppUserID()
- PurchaseService uses customerInfoStream for real-time isPro — no polling
- Sync is push-only (dirty flag upsert). No pull sync. Recipe model is local-only for now (not synced to Supabase — no Supabase table created yet).
- Auth trigger on Supabase inserts into public.users on signup (not pantries). Works correctly.
- PBXFileSystemSynchronizedRootGroup in Xcode project — new Swift files in directory are auto-included, no pbxproj edit needed.

## Known Issues / Todos
- Recipe model has isDirty flag but SyncManager doesn't sync it (local-only). Add Supabase `recipes` table + sync later.
- ShoppingListItem.quantity is Int — fractional amounts (0.5 tsp) get ceiling-rounded to 1. Acceptable for v1.
- Each capture creates new Product records per ingredient — duplicates accumulate. Dedup logic needed later.
- ReorderView.swift still exists but is no longer in the tab shell. Keep for future (pantry depletion post-cook).
- PricesView.swift still exists, dormant.
- Anthropic key embedded client-side — billing risk, must move to edge function before real users.

## Key Decisions
| Date | Decision | Reasoning | Affects |
|------|----------|-----------|---------|
| Pre-session | SwiftData over CoreData | iOS 17+ only, cleaner DX | All models |
| Pre-session | Supabase auth (real emails) | Standard vs synthetic-email model | AuthService, SyncManager |
| Pre-session | Offline-first (SwiftData primary, Supabase sync) | Must work without network | SyncManager dirty-flag pattern |
| Pre-session | Open Food Facts for barcode lookup | Free, no API key | ProductLookupService |
| 2026-04-26 | RevenueCatUI native PaywallView | No-code editable, RC-hosted | PaywallView.swift |
| 2026-04-26 | purchases-ios-spm (not purchases-ios) | User-requested SPM binary target | project.pbxproj |
| 2026-04-26 | Entitlement ID: "Saman Pro" | Must match exactly in code + RC dashboard | PurchaseService.swift |
| 2026-04-26 | Lifetime as Non-Consumable IAP | ASC auto-renewable section doesn't support lifetime | ASC IAP section |
| 2026-04-28 | Free tier: 30 items, 1 list, 1 pantry | Checked at + button level before sheet opens | InventoryView, PantryListView, ShoppingListsView |
| 2026-04-28 | 3-tab shell (Home/Reorder/Lists) | Approved cuts — later swapped Reorder for Recipes | RootView |
| 2026-06-11 | Reposition to recipe capture | Instacart IDP closed; new direction is voice/paste → structured recipe | Whole product direction |
| 2026-06-11 | Path C: add Recipes tab, keep tracker | Ship this week; recipe capture as new headline feature | RootView, new Recipes feature |
| 2026-06-11 | Paste-only capture (no voice v1) | Ship constraint; voice adds Speech framework complexity | RecipeCaptureView |
| 2026-06-11 | No Recipe→Ingredient sub-model | Straight to ShoppingListItems for v1 simplicity | Data model |
| 2026-06-11 | claude-sonnet-4-6 in-app | Harness validated prompt on 4-5; 4-6 is current | RecipeExtractionService |

## Key Files
| File | Purpose |
|------|---------|
| `Saman/App/RootView.swift` | Auth gate + 3-tab shell (Home, Recipes, Lists) |
| `Saman/App/AppEnvironment.swift` | App-wide env: auth, sync, purchases |
| `Saman/Features/Recipes/RecipesView.swift` | Recipes tab — list + empty state |
| `Saman/Features/Recipes/RecipeCaptureView.swift` | Capture sheet — paste → extract → review → push to list |
| `Saman/Core/Services/RecipeExtractionService.swift` | Anthropic API wrapper + extraction prompt |
| `Saman/Core/Services/Config.swift` | Supabase + RC + Anthropic API keys |
| `Saman/Core/Services/PurchaseService.swift` | @Observable RC wrapper, isPro via customerInfoStream |
| `Saman/Core/Services/AuthService.swift` | Supabase auth, pendingEmailConfirmation, resendConfirmation |
| `Saman/Core/Models/Recipe.swift` | SwiftData model for captured recipes |
| `Saman/Core/Persistence/ModelContainer+Setup.swift` | Schema — now includes Recipe.self |
| `Saman/Features/Inventory/InventoryView.swift` | Home tab — pantry tracker |
| `Saman/Features/ShoppingList/ShoppingListsView.swift` | Lists tab |
| `Saman/Features/Settings/PaywallView.swift` | SamanPaywallView wrapper over RC PaywallView |
| `Saman/Features/Auth/AuthView.swift` | Sign in/up + email confirmation |

## Extraction Test Harness
Located at: `saman_capture_test/` (harness.py, extraction.py, fixtures.py, gold.py)
- Run: `cd saman_capture_test && ANTHROPIC_API_KEY=<key> python3 harness.py --run`
- Last run: 2026-06-11 — 0 invented numbers, 100% phrase preservation, 100% code-switch mapping
- Model: claude-sonnet-4-5 (harness default); app uses claude-sonnet-4-6
- IMPORTANT: fixtures are authored, not real phone calls — test on real input before launch

## External Context
- Supabase project: `saman-pantry` (ID: `mcknboqvblbonmaebmjg`, us-east-1) — ACTIVE_HEALTHY
- Bundle ID: `com.samanpantry.Saman`
- Domain: `samanpantry.com`
- RC SDK: purchases-ios-spm v5.69.0 + RevenueCatUI
- RC entitlement: "Saman Pro"
- RC products: Lifetime (one-time), Yearly (subscription), Monthly (subscription)
- ASC Subscription Group: "Saman Pro" (setup in progress)
- Instacart IDP: DEAD — closed, no longer relevant

## Session Log
| Session | Date | Summary |
|---------|------|---------|
| 1 | 2026-04-18 | Initial memory bootstrap. Full codebase read. Product audit. |
| 2 | 2026-04-26 | Privacy page, encryption flag, app icons, full RC integration, ASC product setup started |
| 3 | 2026-04-28 | Auth signup UX, Supabase health check + DB fixes, feature gating, dead code strip, tab restructure, AddPantryView wired, resend confirmation |
| 4 | 2026-06-11 | Phase 0 audit (new direction). Harness run: wall holds, 0 invented numbers. Path C chosen. Built: Recipe model, RecipeExtractionService, RecipesView, RecipeCaptureView. Swapped Reorder tab for Recipes tab. |
