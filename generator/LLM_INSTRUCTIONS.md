# Use Case Template - LLM Instructions (Bilingual EN/FR)

## Overview
You will be provided with a use case description and need to generate a complete **BILINGUAL** HTML page (English + French) using this template. The template uses the INVOKE brand styling with orange (#f36a3d) as the primary accent color, black text on white backgrounds, and professional typography.

## Bilingual System
**CRITICAL:** This template system is fully bilingual. All text content must be provided in BOTH English and French.

- **Variable naming**: All variables end with `_EN` (English) or `_FR` (French) suffix
- **Default language**: English (shown on page load)
- **Toggle functionality**: Users can switch between EN/FR using header buttons
- **Persistence**: Language preference is saved in browser localStorage
- **Data attributes**: Content uses `data-lang-en` and `data-lang-fr` for visibility control

## File Structure (IMPORTANT)
```
use-cases/
├── fonts/                          # Font files
│   ├── font.css                   # Lato font imports
│   └── [font files].woff2
├── generator/                      # Templates and docs
│   ├── usecase_template.html     # This template
│   ├── usecase_style.css         # Shared stylesheet
│   └── LLM_INSTRUCTIONS.md       # This file
├── images/
│   ├── photos/                    # Hero backgrounds
│   └── icons/                     # Feature icons
└── usecases/                       # WHERE YOU SAVE GENERATED FILES
    └── [your-use-case].html       # Your output goes here
```

**CRITICAL PATH INFORMATION:**
When saving to `usecases/` folder, all paths must use `../` to go up one level:
- Fonts: `../fonts/font.css`
- Styles: `../generator/usecase_style.css`
- Images: `../images/photos/` and `../images/icons/`
- Logo: `../images/invoke-logo.svg`

---

## Template Variables to Replace

**TOTAL: 76 variables (38 English + 38 French)**

### Meta Tags (3 - English Only, Required for Homepage)
These appear in the `<head>` section and are used by `update_usecases.py` to generate the homepage. **Only English versions are needed for meta tags.**

- `{{USE_CASE_TITLE_EN}}` - The name of the use case (2-5 words)
  - Example: "Predictive Demand Forecasting"
  - Used in: `<title>` tag and `<meta name="use-case-name">`
  
- `{{USE_CASE_CATEGORY_EN}}` - Industry or functional area
  - Examples: "Supply Chain", "Finance", "Manufacturing", "Healthcare", "Legal", "HR", "Compliance"
  - Used in: `<meta name="use-case-category">`
  - This determines which category filter it appears under on the homepage
  - Keep it simple and consistent: Use "Supply Chain" not "Supply Chain & Logistics" for filtering
  
- `{{USE_CASE_DESCRIPTION_EN}}` - Brief 1-2 sentence description (150-240 characters)
  - Example: "AI-powered demand forecasting that predicts customer needs with 85% accuracy, reducing stockouts and overstock by 40%."
  - Used in: `<meta name="description">`
  - This appears on the homepage card and in search results

**IMPORTANT:** These three English meta tag variables must be filled in every use case for the homepage to work correctly.

### Hero Section (7 variables - 1 shared, 6 bilingual)
- `{{HERO_IMAGE}}` - Select from available photos based on industry/use case (same for both languages)

- `{{INDUSTRY_CATEGORY_EN}}` / `{{INDUSTRY_CATEGORY_FR}}` - Industry or category label for display on page
  - Can be longer/more descriptive than the meta tag category
  - Example EN: "Supply Chain & Logistics" (display on page)
  - Example FR: "Chaîne d'approvisionnement et logistique"
  - vs. Meta tag: "Supply Chain" (for homepage filtering)

- `{{USE_CASE_TITLE_EN}}` / `{{USE_CASE_TITLE_FR}}` - Main heading (2-5 words)
  - Example EN: "Predictive Demand Forecasting"
  - Example FR: "Prévisions de la demande prédictives"

- `{{USE_CASE_DESCRIPTION_EN}}` / `{{USE_CASE_DESCRIPTION_FR}}` - 1-2 sentence value proposition
  - Used in both meta tag and hero section
  - Example EN: "Leverage AI-powered demand forecasting to predict customer needs with 85% accuracy, reducing stockouts and overstock by 40%."
  - Example FR: "Exploitez les prévisions de la demande basées sur l'IA pour prédire les besoins des clients avec une précision de 85 %, réduisant les ruptures de stock et les surstocks de 40 %."

### Challenge/Problem Section (6 variables - all bilingual)
- `{{CHALLENGE_HEADING_EN}}` / `{{CHALLENGE_HEADING_FR}}` - Engaging question or statement
  - Example EN: "Struggling with demand forecasting?"
  - Example FR: "Vous avez du mal avec les prévisions de la demande ?"

- `{{CHALLENGE_INTRO_EN}}` / `{{CHALLENGE_INTRO_FR}}` - 1-2 sentences setting up the problem
  - Example EN: "Traditional forecasting methods leave businesses reactive rather than proactive, leading to costly inventory issues and missed opportunities."
  - Example FR: "Les méthodes de prévision traditionnelles rendent les entreprises réactives plutôt que proactives, entraînant des problèmes d'inventaire coûteux et des opportunités manquées."

- `{{CHALLENGE_ITEMS_EN}}` / `{{CHALLENGE_ITEMS_FR}}` - 4-6 list items, each formatted as:
  ```html
  <li><strong>Challenge Name:</strong> Description of the challenge and its impact.</li>
  ```
  - Example EN:
  ```html
  <li><strong>Inaccurate Forecasts:</strong> Manual forecasting leads to 30% error rates, causing costly stockouts and overstock situations.</li>
  <li><strong>Siloed Data:</strong> Disconnected systems prevent comprehensive demand analysis across channels and regions.</li>
  <li><strong>Slow Response Time:</strong> Monthly forecast cycles can't adapt to rapidly changing market conditions.</li>
  <li><strong>Limited Visibility:</strong> Lack of real-time insights makes it impossible to spot trends until it's too late.</li>
  ```
  - Example FR:
  ```html
  <li><strong>Prévisions inexactes :</strong> Les prévisions manuelles entraînent un taux d'erreur de 30 %, causant des ruptures de stock et des situations de surstock coûteuses.</li>
  <li><strong>Données cloisonnées :</strong> Les systèmes déconnectés empêchent une analyse complète de la demande entre les canaux et les régions.</li>
  <li><strong>Temps de réponse lent :</strong> Les cycles de prévision mensuels ne peuvent pas s'adapter aux conditions de marché en évolution rapide.</li>
  <li><strong>Visibilité limitée :</strong> Le manque d'informations en temps réel rend impossible la détection des tendances avant qu'il ne soit trop tard.</li>
  ```

### How It Works Section (18 variables - all bilingual)

**Subtitle:**
- `{{SOLUTION_SUBTITLE_EN}}` / `{{SOLUTION_SUBTITLE_FR}}` - One sentence explaining what the solution does
  - Example EN: "Transform raw data into actionable demand forecasts"
  - Example FR: "Transformez les données brutes en prévisions de demande exploitables"

**Input Box (6 variables):**
- `{{INPUT_HEADING_EN}}` / `{{INPUT_HEADING_FR}}` - What data/sources are used
  - Example EN: "Data Sources" / Example FR: "Sources de données"
  
- `{{INPUT_DESCRIPTION_EN}}` / `{{INPUT_DESCRIPTION_FR}}` - Brief label
  - Example EN: "Multiple Data Streams" / Example FR: "Flux de données multiples"
  
- `{{INPUT_ITEMS_EN}}` / `{{INPUT_ITEMS_FR}}` - 3-4 list items of specific inputs
  - Format: `<li>Item name</li>`
  - Example EN:
  ```html
  <li>Historical sales data</li>
  <li>Market trends</li>
  <li>Seasonality patterns</li>
  <li>External factors</li>
  ```
  - Example FR:
  ```html
  <li>Données de ventes historiques</li>
  <li>Tendances du marché</li>
  <li>Modèles de saisonnalité</li>
  <li>Facteurs externes</li>
  ```

**Automation Box (4 variables):**
- `{{AUTOMATION_ITEMS_EN}}` / `{{AUTOMATION_ITEMS_FR}}` - 4-5 list items describing automation technologies/processes
  - Format: `<li>Technology or process</li>`
  - Example EN:
  ```html
  <li>Machine learning algorithms</li>
  <li>Pattern recognition</li>
  <li>Anomaly detection</li>
  <li>Predictive modeling</li>
  <li>Automated alerts</li>
  ```
  - Example FR:
  ```html
  <li>Algorithmes d'apprentissage automatique</li>
  <li>Reconnaissance de motifs</li>
  <li>Détection d'anomalies</li>
  <li>Modélisation prédictive</li>
  <li>Alertes automatisées</li>
  ```

- `{{AUTOMATION_DETAIL_EN}}` / `{{AUTOMATION_DETAIL_FR}}` - Key technology explanation
  - Example EN: "Advanced AI models continuously learn from new data to improve accuracy over time."
  - Example FR: "Les modèles d'IA avancés apprennent continuellement à partir de nouvelles données pour améliorer la précision au fil du temps."

**Output Box (6 variables):**
- `{{OUTPUT_HEADING_EN}}` / `{{OUTPUT_HEADING_FR}}` - What is produced
  - Example EN: "Key Benefits" / Example FR: "Avantages clés"
  
- `{{OUTPUT_LABEL_EN}}` / `{{OUTPUT_LABEL_FR}}` - Main deliverable
  - Example EN: "✓ Predictive Dashboard" / Example FR: "✓ Tableau de bord prédictif"
  
- `{{OUTPUT_ITEMS_EN}}` / `{{OUTPUT_ITEMS_FR}}` - 3-4 list items of specific outcomes/benefits
  - Format: `<li>Outcome</li>`
  - Example EN:
  ```html
  <li>Accurate demand forecasts</li>
  <li>Optimized inventory levels</li>
  <li>Proactive decision making</li>
  <li>Real-time visibility</li>
  ```
  - Example FR:
  ```html
  <li>Prévisions de demande précises</li>
  <li>Niveaux d'inventaire optimisés</li>
  <li>Prise de décision proactive</li>
  <li>Visibilité en temps réel</li>
  ```

### Features Section (21 variables - 1 shared, 20 bilingual)

**Section Headers:**
- `{{FEATURES_TITLE_EN}}` / `{{FEATURES_TITLE_FR}}` - Section heading
  - Example EN: "Key Capabilities" / Example FR: "Capacités clés"
  - Alternative EN: "Why Choose Our Solution?" / Alternative FR: "Pourquoi choisir notre solution ?"

- `{{FEATURES_SUBTITLE_EN}}` / `{{FEATURES_SUBTITLE_FR}}` - 1-2 sentences about what makes the solution unique
  - Example EN: "Our platform combines advanced AI with intuitive interfaces to deliver forecasting accuracy that traditional methods can't match."
  - Example FR: "Notre plateforme combine une IA avancée avec des interfaces intuitives pour offrir une précision de prévision que les méthodes traditionnelles ne peuvent égaler."

**For each of 4 feature cards (5 variables per card = 20 total):**
- `{{FEATURE_ICON_N}}` - Icon path (same for both languages, N = 1, 2, 3, 4)
- `{{FEATURE_TITLE_N_EN}}` / `{{FEATURE_TITLE_N_FR}}` - Feature name (2-4 words)
  - Example EN: "Real-Time Analytics" / Example FR: "Analytique en temps réel"
- `{{FEATURE_DESCRIPTION_N_EN}}` / `{{FEATURE_DESCRIPTION_N_FR}}` - 1-2 sentence description
  - Example EN: "Monitor demand patterns as they emerge with live dashboards and instant alerts for anomalies."
  - Example FR: "Surveillez les modèles de demande au fur et à mesure qu'ils émergent avec des tableaux de bord en direct et des alertes instantanées pour les anomalies."

### Value/Results Section (14 variables - all bilingual)

**Section Headers:**
- `{{VALUE_TITLE_EN}}` / `{{VALUE_TITLE_FR}}` - Section title
  - Example EN: "Expected Results" / Example FR: "Résultats attendus"
  - Alternative EN: "Value Delivered" / Alternative FR: "Valeur livrée"

- `{{VALUE_SUBTITLE_EN}}` / `{{VALUE_SUBTITLE_FR}}` - One sentence on business impact
  - Example EN: "Transform your supply chain with measurable improvements across key performance indicators."
  - Example FR: "Transformez votre chaîne d'approvisionnement avec des améliorations mesurables sur les indicateurs de performance clés."

**For each of 4 value cards (3 variables per card = 12 total):**
- `{{VALUE_METRIC_N}}` - The metric itself (N = 1, 2, 3, 4)
  - **Same for both languages** - numbers and symbols don't change
  - Examples: "70%", "$2M", "50 hours", "Real-time", "99.9%"
  
- `{{VALUE_LABEL_N_EN}}` / `{{VALUE_LABEL_N_FR}}` - What the metric represents
  - Example EN: "Reduction in processing time" / Example FR: "Réduction du temps de traitement"
  - Example EN: "Annual cost savings" / Example FR: "Économies de coûts annuelles"
  - Example EN: "Forecast accuracy" / Example FR: "Précision des prévisions"

**Metric Guidelines:**
- Use realistic, achievable numbers (60-90% range for improvements)
- Include a mix of percentages, dollar amounts, time savings, and qualitative benefits
- Be specific: "85% accuracy" not "High accuracy"
- Keep metrics consistent with challenge section promises

**Example Complete Value Cards:**
```
Card 1:
VALUE_METRIC_1: "85%"
VALUE_LABEL_1_EN: "Forecast accuracy"
VALUE_LABEL_1_FR: "Précision des prévisions"

Card 2:
VALUE_METRIC_2: "$2M"
VALUE_LABEL_2_EN: "Annual cost savings"
VALUE_LABEL_2_FR: "Économies de coûts annuelles"

Card 3:
VALUE_METRIC_3: "70%"
VALUE_LABEL_3_EN: "Reduction in stockouts"
VALUE_LABEL_3_FR: "Réduction des ruptures de stock"

Card 4:
VALUE_METRIC_4: "Real-time"
VALUE_LABEL_4_EN: "Demand visibility"
VALUE_LABEL_4_FR: "Visibilité de la demande"
```

### CTA Section (4 variables - all bilingual)
- `{{CTA_TITLE_EN}}` / `{{CTA_TITLE_FR}}` - Call to action heading
  - Example EN: "Ready to Transform Your Operations?"
  - Example FR: "Prêt à transformer vos opérations ?"

- `{{CTA_SUBTITLE_EN}}` / `{{CTA_SUBTITLE_FR}}` - 1-2 sentences encouraging contact
  - Example EN: "Let's discuss how intelligent automation can solve your specific challenges and deliver measurable results."
  - Example FR: "Discutons de la façon dont l'automatisation intelligente peut résoudre vos défis spécifiques et fournir des résultats mesurables."

**Note:** The "Contact Us" / "Contactez-nous" button text is handled automatically in the template.

---

## Available Assets

### Hero Background Photos
Choose the most appropriate image based on the use case industry:

1. `../images/photos/agreement_or_legal.jpg` - Legal/compliance use cases
2. `../images/photos/auto.jpg` - Automotive/manufacturing use cases
3. `../images/photos/business_meeting.jpg` - Business strategy/management use cases
4. `../images/photos/calculating.jpg` - Finance/analytics use cases
5. `../images/photos/cash_kid_with_money.jpg` - Consumer finance use cases
6. `../images/photos/dr_with_clipboard.jpg` - Healthcare/medical use cases
7. `../images/photos/finance.jpg` - Financial services use cases
8. `../images/photos/medical.png` - Healthcare/clinical use cases
9. `../images/photos/paperwork.jpg` - Document processing/administrative use cases
10. `../images/photos/shipping_and_logistics.jpg` - Supply chain/logistics use cases

### Feature Icons
Choose 4 most relevant icons from the available collection:

**AI/ML & Analytics:**
- `../images/icons/ai-robustness.svg` - AI/ML capabilities
- `../images/icons/machine-learning-01.svg` - ML capabilities
- `../images/icons/machine-learning-06.svg` - Advanced ML
- `../images/icons/chart-bubble-line.svg` - Analytics/reporting
- `../images/icons/chart-custom.svg` - Custom analytics
- `../images/icons/chart-multi-type.svg` - Multi-dimensional analysis
- `../images/icons/insights.svg` - Data insights
- `../images/icons/user-analytics.svg` - User analytics

**Automation & Process:**
- `../images/icons/automation-services.svg` - Automation features
- `../images/icons/process.svg` - Process optimization
- `../images/icons/devops.svg` - Development/operations
- `../images/icons/innovate.svg` - Innovation

**Integration & Connectivity:**
- `../images/icons/connect.svg` - Integration capabilities
- `../images/icons/connected-nodes-to-the-cloud.svg` - Connected systems
- `../images/icons/cloud-upload.svg` - Cloud integration
- `../images/icons/network-services.svg` - Network/connectivity
- `../images/icons/it-infrastructure-software.svg` - IT infrastructure
- `../images/icons/server-operating-systems.svg` - System architecture

**Performance & Results:**
- `../images/icons/speedometer.svg` - Performance/speed
- `../images/icons/growth.svg` - Business growth
- `../images/icons/goals.svg` - Goal achievement
- `../images/icons/reduced-cost.svg` - Cost reduction
- `../images/icons/presentation.svg` - Reporting/dashboards

**Security & Support:**
- `../images/icons/protect-critical-assets.svg` - Security
- `../images/icons/customer-service.svg` - User support
- `../images/icons/key-users.svg` - User management

**Other:**
- `../images/icons/notification-user.svg` - Alerts/notifications
- `../images/icons/reset-settings.svg` - Configuration
- `../images/icons/strategy-play.svg` - Strategic planning
- `../images/icons/user-experience-design.svg` - UX/design
- `../images/icons/video-chat.svg` - Collaboration

**Industry-Specific:**
- `../images/icons/hospital.svg` - Healthcare
- `../images/icons/bank.svg` - Banking/Finance
- `../images/icons/capitol.svg` - Government
- `../images/icons/cargo-crane.svg` - Logistics
- `../images/icons/delivery-truck.svg` - Delivery
- `../images/icons/forklift.svg` - Warehousing

---

## Translation Guidelines

### Common English → French Translations

**Section Headers:**
- "How it works" → "Comment ça marche"
- "Key Capabilities" → "Capacités clés"
- "Expected Results" → "Résultats attendus"
- "Contact Us" → "Contactez-nous"
- "Process Details" → "Détails du processus"
- "Why Choose Our Solution?" → "Pourquoi choisir notre solution ?"

**Common Business Terms:**
- Automation → Automatisation
- Intelligence → Intelligence
- Data → Données
- Process → Processus
- Efficiency → Efficacité
- Accuracy → Précision
- Real-time → Temps réel
- Analytics → Analytique
- Dashboard → Tableau de bord
- Integration → Intégration
- Solution → Solution
- System → Système
- Platform → Plateforme
- Technology → Technologie
- Innovation → Innovation

**Action Verbs:**
- Transform → Transformer
- Optimize → Optimiser
- Automate → Automatiser
- Predict → Prédire
- Analyze → Analyser
- Monitor → Surveiller
- Improve → Améliorer
- Reduce → Réduire
- Increase → Augmenter

**Metrics & Results:**
- "Reduction in" → "Réduction de"
- "Increase in" → "Augmentation de"
- "Improvement in" → "Amélioration de"
- "Faster" → "Plus rapide"
- "Annual savings" → "Économies annuelles"
- "Cost savings" → "Économies de coûts"
- "Processing time" → "Temps de traitement"
- "Accuracy rate" → "Taux de précision"

**Keep the Same:**
- Numbers: "70%", "$2M", "85%" (don't translate)
- Proper nouns: "INVOKE" (brand name)
- Technical abbreviations: "AI", "ML", "API" (commonly used internationally)

### French Translation Quality Standards
- Use **proper French business terminology**
- Maintain **professional, formal tone** (use "vous" not "tu")
- Ensure **natural phrasing**, not literal/robotic translation
- Use **Canadian French** spelling and conventions where applicable
- **Accent marks** are required: é, è, ê, à, ç, etc.
- **Numbers**: Use space as thousand separator in French: "2 000" not "2,000"

---

## Content Guidelines

### Tone & Style
- **Professional** but approachable
- Focus on **business value** and measurable outcomes
- Use **specific, measurable** benefits when possible (not vague claims)
- Avoid overly technical jargon (make it accessible to business stakeholders)
- Keep descriptions **concise** and impactful
- Use **active voice** (not passive)

### Structure Best Practices
1. **Hero**: Hook the reader immediately with clear value proposition
2. **Challenges**: Relate to common pain points they experience (empathy)
3. **How It Works**: Show the transformation from inputs to outputs (clarity)
4. **Features**: Highlight unique differentiators (competitive advantage)
5. **Value**: Quantify results with realistic metrics (proof)
6. **CTA**: Create urgency without being pushy (invitation)

### Metrics Best Practices
**Do:**
- Use realistic ranges: 60-90% for improvements
- Include mix of types: percentages, dollars, time, qualitative
- Be specific: "85% accuracy" not "high accuracy"
- Show business impact: "$2M annual savings" not just "saves money"
- Use round numbers: "70%" not "73.4%"

**Don't:**
- Over-promise: Claiming "100% accuracy" is not credible
- Use vague terms: "significant improvement" - quantify it!
- Ignore context: "$2M savings" needs scale context
- Forget consistency: Metrics should align with challenges

**Example Good Metrics:**
- Percentages: "85%", "40%", "99.9%", "70%"
- Dollar amounts: "$2M", "$500K", "$750K"
- Time: "50 hours per week", "3 days", "Real-time", "24/7"
- Qualitative: "100% audit-ready", "Scalable to any volume", "Zero manual entry"

---

## Example Transformation

**Input Prompt:** "Create a bilingual use case for predictive maintenance in manufacturing equipment"

**Output Variables (Sample):**

### Meta Tags:
```
USE_CASE_TITLE_EN: "Predictive Equipment Maintenance"
USE_CASE_CATEGORY_EN: "Manufacturing"
USE_CASE_DESCRIPTION_EN: "Prevent costly downtime and extend equipment life with AI-powered predictive maintenance that identifies potential failures before they occur."
```

### Hero Section:
```
HERO_IMAGE: "../images/photos/auto.jpg"

INDUSTRY_CATEGORY_EN: "Manufacturing & Operations"
INDUSTRY_CATEGORY_FR: "Fabrication et opérations"

USE_CASE_TITLE_EN: "Predictive Equipment Maintenance"
USE_CASE_TITLE_FR: "Maintenance prédictive des équipements"

USE_CASE_DESCRIPTION_EN: "Prevent costly downtime and extend equipment life with AI-powered predictive maintenance that identifies potential failures before they occur."
USE_CASE_DESCRIPTION_FR: "Évitez les temps d'arrêt coûteux et prolongez la durée de vie des équipements grâce à la maintenance prédictive basée sur l'IA qui identifie les défaillances potentielles avant qu'elles ne se produisent."
```

### Challenge Section:
```
CHALLENGE_HEADING_EN: "Equipment failures costing you millions?"
CHALLENGE_HEADING_FR: "Les pannes d'équipement vous coûtent-elles des millions ?"

VALUE_METRIC_1: "60%"
VALUE_LABEL_1_EN: "Reduction in unplanned downtime"
VALUE_LABEL_1_FR: "Réduction des temps d'arrêt non planifiés"
```

---

## Output Format Requirements

Your output must:
1. ✅ Be complete, production-ready HTML
2. ✅ Have ALL 76 variables replaced (38 EN + 38 FR)
3. ✅ Remove ALL instruction comments
4. ✅ Use correct file paths (`../` from usecases folder)
5. ✅ Include natural French translations (not literal/robotic)
6. ✅ Have proper list formatting (`<li>` items)
7. ✅ Use appropriate hero image for the industry
8. ✅ Select 4 relevant feature icons
9. ✅ Include realistic metrics (60-90% range)
10. ✅ Maintain INVOKE brand colors (#f36a3d for orange)

**Do NOT include:**
- Template instruction comments in output
- {{VARIABLE}} placeholders (all must be replaced)
- Placeholder text like "Lorem ipsum"
- Generic/vague content

---

## Visual Process Diagram (Optional)

You may include a custom SVG diagram between the "How it works" title and the process boxes. This is optional but recommended for visual impact.

**6 Diagram Types Available:**
1. **Linear Flow** - Simple sequential: Input → Processing → Output
2. **Multi-Input Pipeline** - Multiple sources → Processing → Output
3. **Cycle Diagram** - Continuous loop
4. **Decision Tree** - Branching logic
5. **Hub & Spoke** - Central system with connections
6. **Layered Architecture** - Stacked tiers

**Design Guidelines:**
- Use INVOKE orange (#f36a3d) for arrows and emphasis
- Use viewBox for responsiveness: `viewBox="0 0 1000 400"`
- Keep labels short (2-4 words per box)
- See template comments for example SVG structure

**If you include a diagram, you MUST include the separator:**
The bilingual separator HTML is already in the template showing:
- English: "PROCESS DETAILS"
- French: "DÉTAILS DU PROCESSUS"

---

## Categories for Meta Tag

Use consistent, simple categories for the `USE_CASE_CATEGORY_EN` meta tag:

**Recommended Categories:**
- Supply Chain
- Finance
- Manufacturing
- Healthcare
- Legal
- HR
- Compliance
- Customer Service
- Operations
- IT & DevOps
- Marketing
- Sales

Keep categories simple for homepage filtering. Use more descriptive text in `INDUSTRY_CATEGORY_EN/FR` for page display.

---

## Final Checklist Before Output

Before returning your generated HTML, verify:

- [ ] All 76 variables replaced (38 EN + 38 FR)
- [ ] Meta tags filled (English only)
- [ ] Hero image selected and path correct
- [ ] 4 feature icons selected and paths correct
- [ ] French translations are natural (not literal)
- [ ] Metrics are realistic (60-90%)
- [ ] All instruction comments removed
- [ ] File paths use `../` correctly
- [ ] List items properly formatted with `<li>` tags
- [ ] CTA section encourages action
- [ ] Bilingual toggle will work (data-lang attributes correct)

---

## Questions?

If you're unsure about any variable, refer to:
- The template HTML for structure
- This file for variable definitions
- The example transformation above
- The translation guide for French terms

**Remember:** Every piece of visible text needs both EN and FR versions!