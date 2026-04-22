# February 2026

## Styling and dashboard updates

### Pull #348 https://github.com/ruyisdk/ruyisdk-website/pull/348
- Revert the stats/dashboard page to the previous design while keeping updated functionality.
- Replace CSS-module based styles with Tailwind utility classes and minimal custom CSS for charts and orbit layout.
- Adjust statistics, charts, and mobile install sections to use simpler card layouts with updated typography and spacing.
- Extract complex FlipCounter styles into a standalone CSS file and update its usage.
- Integrate a reusable PageBackground component and simplify the page container styling.
- Status: merged (merged_at: 2026-02-02).

### Pull #354 https://github.com/ruyisdk/ruyisdk-website/pull/354
- Migrate the site styling pipeline from UnoCSS to Tailwind CSS.
- Add Tailwind configuration, PostCSS setup (autoprefixer), and Tailwind entry CSS; remove UnoCSS plugin and related files.
- Introduce new shared visual pieces (e.g., AnimatedBlobs background component) and tune homepage/card typography and button styles.
- Update Docusaurus configuration to load Tailwind styles.
- Status: open (work-in-progress; active Tailwind migration and style tuning).

### Pull #371 https://github.com/ruyisdk/ruyisdk-website/pull/371
- Remove remaining Ant Design (antd) components and @ant-design/icons usages across the UI.
- Replace antd layout/components (Tabs, Card, Tag, Button, modal close icon, Progress, etc.) with lightweight custom HTML/CSS equivalents and lucide-react icons.
- Implement a custom progress bar for category statistics and update FlipCounter/empty states to use lucide-react icons.
- Remove antd and @ant-design/icons from package.json and clean up unused imports (dashboard, QRCode, etc.).
- Adjust responsive styles for stats and charts to match new grid-based layouts and custom cards/buttons.
- Status: open (major UI/dependency removal in progress).

### Pull #383 https://github.com/ruyisdk/ruyisdk-website/pull/383
- Disable dark mode for CodeBlock
