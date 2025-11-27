# Use Case Template - LLM Instructions

## Overview
You will be provided with a use case description and need to generate a complete HTML page using this template. The template uses the INVOKE brand styling with orange (#f36a3d) as the primary accent color, black text on white backgrounds, and professional typography.

## Template Variables to Replace

### Page Title Section
- `{{USE_CASE_TITLE}}` - The name of the use case (2-5 words, e.g., "Predictive Demand Forecasting")

### Hero Section
- `{{HERO_IMAGE}}` - Select from available photos based on industry/use case
- `{{INDUSTRY_CATEGORY}}` - Industry or category label (e.g., "Supply Chain & Logistics", "Healthcare Solutions", or default "Intelligent Automation & Digital Transformation")
- `{{USE_CASE_DESCRIPTION}}` - 1-2 sentence value proposition

### Challenge/Problem Section
- `{{CHALLENGE_HEADING}}` - Engaging question or statement (e.g., "Struggling with demand forecasting?")
- `{{CHALLENGE_INTRO}}` - 1-2 sentences setting up the problem
- `{{CHALLENGE_ITEMS}}` - 4-6 list items, each formatted as:
  ```html
  <li><strong>Challenge Name:</strong> Description of the challenge and its impact.</li>
  ```

### How It Works Section
- `{{SOLUTION_SUBTITLE}}` - One sentence explaining what the solution does
- **Input Box:**
  - `{{INPUT_HEADING}}` - e.g., "Data Sources", "Input Systems"
  - `{{INPUT_DESCRIPTION}}` - Brief label, e.g., "Multiple Data Streams"
  - `{{INPUT_ITEMS}}` - 3-4 list items: `<li>Item name</li>`
- **Automation Box:**
  - `{{AUTOMATION_ITEMS}}` - 4-5 list items describing technologies
  - `{{AUTOMATION_DETAIL}}` - Key technology explanation
- **Output Box:**
  - `{{OUTPUT_HEADING}}` - e.g., "Key Benefits", "Results"
  - `{{OUTPUT_LABEL}}` - Main deliverable, e.g., "✓ Predictive Dashboard"
  - `{{OUTPUT_ITEMS}}` - 3-4 list items of outcomes

### Features Section
- `{{FEATURES_TITLE}}` - Section heading (e.g., "Key Capabilities")
- `{{FEATURES_SUBTITLE}}` - 1-2 sentences on uniqueness
- For 4 feature cards:
  - `{{FEATURE_ICON_N}}` - Icon path from available icons
  - `{{FEATURE_TITLE_N}}` - Feature name (2-4 words)
  - `{{FEATURE_DESCRIPTION_N}}` - 1-2 sentence description

### Value/Results Section
- `{{VALUE_TITLE}}` - e.g., "Expected Results", "Value Delivered"
- `{{VALUE_SUBTITLE}}` - One sentence on impact
- For 4 value cards:
  - `{{VALUE_METRIC_N}}` - Metric (e.g., "70%", "$2M", "Real-time")
  - `{{VALUE_LABEL_N}}` - What the metric represents

### CTA Section
- `{{CTA_TITLE}}` - Call to action heading
- `{{CTA_SUBTITLE}}` - 1-2 sentences encouraging contact

## Available Assets

### Hero Background Photos
Choose the most appropriate:
1. `../images/photos/agreement_or_legal.jpg` - Legal/compliance
2. `../images/photos/auto.jpg` - Automotive/manufacturing
3. `../images/photos/business_meeting.jpg` - Business strategy
4. `../images/photos/calculating.jpg` - Finance/analytics
5. `../images/photos/cash_kid_with_money.jpg` - Consumer finance
6. `../images/photos/dr_with_clipboard.jpg` - Healthcare
7. `../images/photos/finance.jpg` - Financial services
8. `../images/photos/medical.png` - Healthcare/clinical
9. `../images/photos/paperwork.jpg` - Document processing
10. `../images/photos/shipping_and_logistics.jpg` - Supply chain/logistics

### Feature Icons
Choose 4 most relevant icons:
- `../images/icons/ai-robustness.svg` - AI/ML capabilities
- `../images/icons/automation-services.svg` - Automation features
- `../images/icons/chart-bubble-line.svg` - Analytics/reporting
- `../images/icons/chart-custom.svg` - Custom analytics
- `../images/icons/chart-multi-type.svg` - Multi-dimensional analysis
- `../images/icons/cloud-upload.svg` - Cloud integration
- `../images/icons/connect.svg` - Integration capabilities
- `../images/icons/connected-nodes-to-the-cloud.svg` - Connected systems
- `../images/icons/customer-service.svg` - User support
- `../images/icons/devops.svg` - Development/operations
- `../images/icons/goals.svg` - Goal achievement
- `../images/icons/growth.svg` - Business growth
- `../images/icons/innovate.svg` - Innovation
- `../images/icons/insights.svg` - Data insights
- `../images/icons/it-infrastructure-software.svg` - IT infrastructure
- `../images/icons/key-users.svg` - User management
- `../images/icons/machine-learning-01.svg` - ML capabilities
- `../images/icons/machine-learning-06.svg` - Advanced ML
- `../images/icons/network-services.svg` - Network/connectivity
- `../images/icons/notification-user.svg` - Alerts/notifications
- `../images/icons/presentation.svg` - Reporting/dashboards
- `../images/icons/process.svg` - Process optimization
- `../images/icons/protect-critical-assets.svg` - Security
- `../images/icons/reduced-cost.svg` - Cost reduction
- `../images/icons/reset-settings.svg` - Configuration
- `../images/icons/server-operating-systems.svg` - System architecture
- `../images/icons/speedometer.svg` - Performance/speed
- `../images/icons/strategy-play.svg` - Strategic planning
- `../images/icons/user-analytics.svg` - User analytics
- `../images/icons/user-experience-design.svg` - UX/design
- `../images/icons/video-chat.svg` - Collaboration

## Content Guidelines

### Tone & Style
- Professional but approachable
- Focus on business value and outcomes
- Use specific, measurable benefits when possible
- Avoid overly technical jargon
- Keep descriptions concise and impactful

### Structure Best Practices
1. **Hero**: Hook the reader immediately with clear value proposition
2. **Challenges**: Relate to common pain points they experience
3. **How It Works**: Show the transformation from inputs to outputs
4. **Features**: Highlight unique differentiators
5. **Value**: Quantify results with realistic metrics
6. **CTA**: Create urgency without being pushy

### Metrics Examples
- Percentages: "85%", "40%", "99%"
- Dollar amounts: "$2M", "$500K"
- Time savings: "50 hours", "3 days"
- Qualitative: "Real-time", "Scalable", "Automated"

## Example Transformation

**Input:** "Predictive maintenance for manufacturing equipment"

**Output Variables:**
- `USE_CASE_TITLE`: "Predictive Equipment Maintenance"
- `HERO_IMAGE`: "../images/photos/auto.jpg"
- `INDUSTRY_CATEGORY`: "Manufacturing & Operations"
- `USE_CASE_DESCRIPTION`: "Prevent costly downtime and extend equipment life with AI-powered predictive maintenance that identifies potential failures before they occur."
- `CHALLENGE_HEADING`: "Equipment failures costing you millions?"
- `VALUE_METRIC_1`: "60%"
- `VALUE_LABEL_1`: "Reduction in unplanned downtime"
- etc.

## Output Format
Return only the complete HTML with all `{{VARIABLES}}` replaced with actual content. Remove all instruction comments. Ensure all paths are correct and all list items are properly formatted.
