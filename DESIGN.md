# Design System Strategy: ICETME–2027

## 1. Overview & Creative North Star
**Creative North Star: "The Hyper-Academic Prism"**

Traditional academic websites often feel static, dense, and dated. This design system rejects the "document-heavy" aesthetic in favor of a **Hyper-Academic Prism**. We are building a digital experience that feels like a high-end research facility: translucent, multidimensional, and mathematically precise. 

To break the "template" look, we move away from rigid, boxed-in grids. Instead, we utilize **intentional asymmetry**, where content floats on layered glass planes. By overlapping typography and using deep z-axis stacking, we create a sense of physical space and futuristic momentum appropriate for ICETME–2027.

---

## 2. Colors & Surface Logic
The palette is rooted in deep intellectual blues and clean, expansive whites, punctuated by gradients that mimic the refraction of light through glass.

### The "No-Line" Rule
**Explicit Instruction:** Do not use 1px solid borders to define sections. Structural boundaries must be created through background shifts or tonal transitions. 
- Use `surface` (#f7f9fb) as your base canvas.
- Use `surface-container-low` (#f2f4f6) for major sectioning.
- The absence of lines forces a "liquid" layout that feels more modern and premium.

### Surface Hierarchy & Nesting
Think of the UI as a physical stack of materials. 
- **Tier 1 (Base):** `surface`
- **Tier 2 (The Inset):** `surface-container-lowest` (#ffffff) for the main content area.
- **Tier 3 (The Pop):** `surface-container-high` (#e6e8ea) for interactive callouts.

### The "Glass & Gradient" Rule
To achieve the "Futuristic" requirement, use Glassmorphism for floating UI elements (like Navigation Bars or Speaker Cards).
- **Glass Recipe:** `surface_container_lowest` at 70% opacity + `backdrop-blur: 20px`.
- **Signature Gradients:** For primary CTAs, use a linear gradient from `primary` (#003ec7) to `primary_container` (#0052ff). This adds "visual soul" and prevents the design from feeling flat.

---

## 3. Typography: The Editorial Edge
We use a high-contrast pairing to balance technical precision with readability.

- **Display & Headlines (Space Grotesk):** This is our "Tech" voice. Use `display-lg` (3.5rem) with tight letter-spacing (-0.02em) for hero sections. The geometric nature of Space Grotesk provides the futuristic edge.
- **Body & Titles (Inter):** This is our "Academic" voice. Inter provides world-class legibility for dense research abstracts. 
- **Intentional Scale:** Do not be afraid of the "Big and Small" approach. Pair a `display-lg` headline with a `label-md` uppercase sub-header to create an editorial, high-fashion layout.

---

## 4. Elevation & Depth
Depth is not a "style"—it is a functional tool for hierarchy.

- **The Layering Principle:** Place a `surface-container-lowest` card atop a `surface-container-low` background. This creates a natural "lift" without the visual clutter of a shadow.
- **Ambient Shadows:** When an element must "float" (e.g., a modal or a primary CTA), use an ambient shadow. 
    - **Color:** Use `on-surface` (#191c1e) at 6% opacity.
    - **Blur:** 32px to 64px for a soft, diffused look. Avoid "tight" shadows.
- **The "Ghost Border" Fallback:** If a container needs a boundary for accessibility, use the `outline-variant` (#c3c5d9) at **15% opacity**. It should be felt, not seen.
- **Glassmorphism Depth:** Use a subtle `primary_fixed` (#dde1ff) inner glow (1px) on glass cards to simulate light hitting the edge of a lens.

---

## 5. Components

### Buttons
- **Primary:** Gradient fill (`primary` to `primary_container`), `xl` (1.5rem) roundedness. Use `on_primary` for text.
- **Secondary (Glass):** `surface_container_lowest` at 40% opacity + 12px blur + 1px ghost border. 
- **States:** On hover, increase the gradient intensity and add a subtle `0.5rem` lift using an ambient shadow.

### Cards (The Research Prism)
- **Rules:** No dividers. Separate the "Abstract" text from the "Author" label using a `surface_container_highest` background shift for the footer of the card.
- **Interaction:** On hover, the card should scale slightly (1.02x) and the ghost border should shift from 15% to 40% opacity.

### Navigation (The Floating Hub)
- **Style:** A floating pill shape using `full` roundedness. 
- **Material:** Glassmorphic `surface_container_low` with a 20px backdrop blur.
- **Active State:** Instead of an underline, use a small `primary` dot below the text or a subtle `primary_fixed` background capsule.

### Inputs & Fields
- **Background:** `surface_container_lowest`.
- **Active State:** 2px stroke of `primary` (#003ec7).
- **Error:** `error` (#ba1a1a) text with `error_container` background tint.

### Conference Timeline (The Chronos List)
- **Style:** Avoid standard tables. Use a vertical "Asymmetric List." 
- **Logic:** Time stamps in `title-lg` (Space Grotesk) on the left, with the event details in an overlapping `surface-container-low` card on the right.

---

## 6. Do's and Don'ts

### Do:
- **Use White Space as a Tool:** Give the content room to breathe. Academic content is dense; the UI shouldn't be.
- **Overlap Elements:** Let a "floating glass" card slightly overlap a headline to create depth.
- **Use Sub-pixel Motion:** Use `cubic-bezier(0.4, 0, 0.2, 1)` for all transitions. It should feel "oiled" and expensive.

### Don't:
- **No Pure Black Shadows:** Never use `#000000` for shadows; always use a tint of the `on-surface` color.
- **No 1px Borders:** Avoid them at all costs. Use background color steps to define hierarchy.
- **No Default Grids:** Don't just center everything. Try left-aligned headlines with right-aligned body copy to create a sophisticated, asymmetrical tension.
- **No Generic Icons:** Use ultra-thin (1pt or 1.5pt) stroke icons to match the Inter/Space Grotesk aesthetic. No filled, "chunky" icons.