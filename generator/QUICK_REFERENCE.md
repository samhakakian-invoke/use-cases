# Use Case Template System - Quick Reference

## Files Created

1. **usecase_template.html** - The main template with {{VARIABLES}} placeholders and embedded instructions
2. **usecase_style.css** - The stylesheet (shared across all use cases)
3. **LLM_INSTRUCTIONS.md** - Comprehensive guide for LLMs on how to use the template
4. **example-demand-forecasting.html** - A complete example showing the template in action

## How to Use

### For LLM Generation

**Prompt Format:**
```
Using the provided usecase_template.html and following the instructions in LLM_INSTRUCTIONS.md, 
create a use case page for:

[USE CASE DESCRIPTION]

Example: "Automated invoice processing for accounts payable departments"
```

The LLM will:
1. Read the template structure
2. Select appropriate hero image from available photos
3. Choose 4 relevant icons for features
4. Fill in all {{VARIABLES}} with contextually appropriate content
5. Return complete HTML ready to save

### Variable Replacement Checklist

**Hero Section (4 variables)**
- [ ] USE_CASE_TITLE
- [ ] HERO_IMAGE (from photos list)
- [ ] INDUSTRY_CATEGORY  
- [ ] USE_CASE_DESCRIPTION

**Challenge Section (3 variables)**
- [ ] CHALLENGE_HEADING
- [ ] CHALLENGE_INTRO
- [ ] CHALLENGE_ITEMS (4-6 list items)

**How It Works Section (9 variables)**
- [ ] SOLUTION_SUBTITLE
- [ ] INPUT_HEADING, INPUT_DESCRIPTION, INPUT_ITEMS
- [ ] AUTOMATION_ITEMS, AUTOMATION_DETAIL
- [ ] OUTPUT_HEADING, OUTPUT_LABEL, OUTPUT_ITEMS

**Features Section (10 variables)**
- [ ] FEATURES_TITLE, FEATURES_SUBTITLE
- [ ] FEATURE_ICON_1 through FEATURE_ICON_4
- [ ] FEATURE_TITLE_1 through FEATURE_TITLE_4
- [ ] FEATURE_DESCRIPTION_1 through FEATURE_DESCRIPTION_4

**Value Section (10 variables)**
- [ ] VALUE_TITLE, VALUE_SUBTITLE
- [ ] VALUE_METRIC_1 through VALUE_METRIC_4
- [ ] VALUE_LABEL_1 through VALUE_LABEL_4

**CTA Section (2 variables)**
- [ ] CTA_TITLE
- [ ] CTA_SUBTITLE

**Total: 38 variables to replace**

## Asset Quick Reference

### Photos (Choose 1 for Hero)
```
Legal/Compliance:     ../images/photos/agreement_or_legal.jpg
Manufacturing:        ../images/photos/auto.jpg
Business/Strategy:    ../images/photos/business_meeting.jpg
Finance/Analytics:    ../images/photos/calculating.jpg
Consumer Finance:     ../images/photos/cash_kid_with_money.jpg
Healthcare:           ../images/photos/dr_with_clipboard.jpg
Financial Services:   ../images/photos/finance.jpg
Clinical:             ../images/photos/medical.png
Documents/Admin:      ../images/photos/paperwork.jpg
Supply Chain:         ../images/photos/shipping_and_logistics.jpg
```

### Icons (Choose 4 for Features)
Common selections by category:

**AI/ML/Analytics:**
- ai-robustness.svg
- machine-learning-01.svg
- chart-custom.svg
- insights.svg

**Automation/Integration:**
- automation-services.svg
- connect.svg
- devops.svg
- process.svg

**Performance/Results:**
- speedometer.svg
- growth.svg
- reduced-cost.svg
- goals.svg

**Reporting/Visibility:**
- presentation.svg
- user-analytics.svg
- chart-multi-type.svg
- notification-user.svg

## File Structure

When deploying, maintain this structure:
```
usecases/
├── usecase_style.css
├── fonts/
│   ├── font.css
│   ├── light.woff2
│   ├── regular.woff2
│   └── bold.woff2
├── [use-case-name].html
├── [use-case-name-2].html
└── [use-case-name-3].html

images/
├── invoke-logo.svg
├── invoke-circle-divider.svg
├── photos/
│   └── [all photo files]
└── icons/
    └── [all icon files]
```

## Example Prompts for Different Use Cases

**Manufacturing:**
"Create a use case page for predictive equipment maintenance in manufacturing facilities, focusing on reducing downtime and extending asset life"

**Healthcare:**
"Create a use case page for automated patient appointment scheduling and reminders in healthcare clinics"

**Finance:**
"Create a use case page for automated fraud detection in credit card transactions using machine learning"

**Logistics:**
"Create a use case page for route optimization for delivery fleet management"

**HR:**
"Create a use case page for automated resume screening and candidate matching for recruitment"

## Quality Checklist

Before finalizing:
- [ ] All {{VARIABLES}} replaced (no placeholders remain)
- [ ] Hero image appropriate for industry
- [ ] 4 relevant icons selected for features
- [ ] Challenge items are specific and relatable
- [ ] Value metrics are realistic and measurable
- [ ] All paths correct (../ for images from usecases folder)
- [ ] Content flows logically from problem → solution → features → results
- [ ] Tone is professional but approachable
- [ ] No instruction comments remain in final HTML

## Tips for Best Results

1. **Be Specific**: Vague descriptions lead to generic content. Provide industry context.
2. **Show Value**: Focus on measurable business outcomes, not just features.
3. **Match Icons**: Icon selection should visually represent the feature described.
4. **Photo Selection**: Hero photo sets the tone - choose carefully for industry fit.
5. **Realistic Metrics**: Use believable percentages (60-90% range for improvements).
6. **Consistent Voice**: Maintain professional yet accessible tone throughout.
