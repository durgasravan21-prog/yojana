# -*- coding: utf-8 -*-
import os
import sys

path = r'c:\Users\durga\OneDrive\Desktop\yojana'

# The 50 schemes to keep
KEEP_SCHEMES = {
    'pm-kisan', 'pm-fasal-bima', 'kisan-credit-card', 'soil-health-card', 'paramparagat-krishi',
    'ayushman-bharat', 'pm-jan-aushadhi', 'mission-indradhanush', 'janani-suraksha', 'jssk',
    'pm-awas', 'pm-awas-urban', 'pm-surya-ghar', 'saubhagya',
    'samagra-shiksha', 'pm-shri-schools', 'pmrf', 'national-overseas-scholarship', 'pragati-scholarship',
    'sukanya-samriddhi', 'lakhpati-didi', 'beti-bachao', 'mission-shakti', 'mahila-shakti-kendra',
    'jan-dhan', 'mudra-yojana', 'stand-up-india', 'pmegp', 'cgtmse-scheme',
    'mgnrega', 'pm-kaushal-vikas', 'national-career-service', 'national-apprenticeship', 'garib-kalyan-rojgar',
    'atal-pension', 'pm-shram-yogi', 'pm-kisan-maandhan', 'varishtha-pension', 'pmvvy',
    'jal-jeevan-mission', 'swachh-bharat', 'pm-gram-sadak', 'rurban-mission',
    'ujala-scheme', 'ujjwala-yojana', 'national-solar-mission',
    'smart-cities', 'amrut', 'gati-shakti',
    'national-food-security'
}

# Load SCHEMES from generate_schemes.py
sys.path.append(path)
try:
    from generate_schemes import SCHEMES as CURATED_SCHEMES, CATEGORIES as CURATED_CATEGORIES
    print(f"Loaded {len(CURATED_SCHEMES)} curated schemes from generate_schemes.py")
except Exception as e:
    print(f"Error loading from generate_schemes.py: {e}")
    CURATED_SCHEMES = []

# Load Base Schemes list from generate_280_schemes.py
try:
    from generate_280_schemes import get_base_schemes
    BASE_280_LIST = get_base_schemes()
    print(f"Loaded {len(BASE_280_LIST)} base schemes from generate_280_schemes.py")
except Exception as e:
    print(f"Error loading from generate_280_schemes.py: {e}")
    BASE_280_LIST = []

# Override details for the 33 schemes (not in generate_schemes.py) to make them rich & factual
SCHEME_FACTS = {
    "pm-awas-urban": {
        "fullname": "Pradhan Mantri Awas Yojana - Urban (PMAY-U)",
        "portal": "https://pmay-urban.gov.in",
        "benefit": "Financial assistance up to ₹2.67 Lakh through Credit Linked Subsidy Scheme (CLSS) on home loans, or direct central assistance of ₹1.5 Lakh under Beneficiary Led Construction (BLC) for building pucca houses.",
        "eligibility": [
            "Families belonging to Economically Weaker Sections (EWS), Low Income Groups (LIG), or Middle Income Groups (MIG).",
            "The beneficiary family should not own a pucca house in their name anywhere in India.",
            "A beneficiary family unit comprises husband, wife, and unmarried children."
        ],
        "faqs": [
            {"q": "What is the household income limit for EWS category under PMAY-U?", "a": "The annual household income limit for the Economically Weaker Section (EWS) category is up to ₹3,00,000 per annum."},
            {"q": "Can women apply for PMAY-U home loans?", "a": "Yes, female ownership or co-ownership of the house is mandatory for the EWS and LIG categories under the scheme guidelines."},
            {"q": "How is the subsidy amount paid?", "a": "The interest subsidy is calculated upfront and credited directly to the beneficiary's loan account, reducing the outstanding principal amount and monthly EMI."}
        ]
    },
    "pm-kisan-maandhan": {
        "fullname": "Pradhan Mantri Kisan Maandhan Yojana (PM-KMY)",
        "portal": "https://maandhan.in",
        "benefit": "An assured monthly pension of ₹3,000 to eligible small and marginal farmers after they reach the age of 60 years. It is a voluntary and contributory pension scheme.",
        "eligibility": [
            "Small and marginal farmers who own cultivable land up to 2 hectares as per state land records.",
            "Entry age group must be between 18 and 40 years.",
            "Should not be covered under any other social security or statutory pension scheme."
        ],
        "faqs": [
            {"q": "What is the monthly contribution under PM Kisan Maandhan?", "a": "The monthly contribution ranges from ₹55 to ₹200 based on the entry age of the farmer. The Central Government makes an equal matching contribution to the pension fund."},
            {"q": "What happens if the beneficiary dies after age 60?", "a": "If the pensioner dies, the spouse is entitled to receive 50% of the pension (₹1,500/month) as family pension, provided they are not already a beneficiary themselves."},
            {"q": "Can I withdraw from the pension scheme early?", "a": "Yes, you can exit the scheme after 5 years of regular contributions, and your savings will be returned with interest equal to the prevailing bank savings rate."}
        ]
    },
    "varishtha-pension": {
        "fullname": "Varishtha Pension Bima Yojana (VPBY)",
        "portal": "https://licindia.in",
        "benefit": "A social security scheme for senior citizens providing an assured pension based on a guaranteed rate of return of 8% per annum. The pension can be received monthly, quarterly, half-yearly, or annually.",
        "eligibility": [
            "Must be a senior citizen aged 60 years or above.",
            "No maximum age limit for entry into the pension program.",
            "The policy must be purchased from Life Insurance Corporation of India (LIC)."
        ],
        "faqs": [
            {"q": "Who administers the Varishtha Pension Bima Yojana?", "a": "The scheme is administered exclusively by the Life Insurance Corporation of India (LIC) under guidelines issued by the Ministry of Finance."},
            {"q": "Is there a premature exit option?", "a": "Yes, premature surrender of the policy is allowed after 15 years, or in case of critical illness of the pensioner or spouse, with a refund of 98% of the purchase price."},
            {"q": "Can I take a loan against the VPBY policy?", "a": "Yes, loan facilities are available after completing 3 policy years, up to a maximum of 75% of the purchase price."}
        ]
    },
    "pmvvy": {
        "fullname": "Pradhan Mantri Vaya Vandana Yojana (PMVVY)",
        "portal": "https://licindia.in",
        "benefit": "A pension scheme for senior citizens offering an assured rate of return of 7.4% per annum. Senior citizens can invest up to a maximum of ₹15 Lakh to secure a stable monthly income.",
        "eligibility": [
            "Must be an Indian citizen aged 60 years or older.",
            "Minimum policy term is 10 years.",
            "Maximum purchase price per senior citizen is limited to ₹15 Lakh."
        ],
        "faqs": [
            {"q": "What is the maximum monthly pension under PMVVY?", "a": "The maximum monthly pension is ₹9,250 for an investment of ₹15 Lakh, and the minimum pension is ₹1,000 per month for an investment of ₹1.62 Lakh."},
            {"q": "Is PMVVY taxable?", "a": "The pension payments received under PMVVY are subject to income tax according to the tax slabs of the beneficiary; however, the purchase price is tax-free on maturity."},
            {"q": "What happens on maturity after 10 years?", "a": "On survival of the pensioner to the end of the policy term of 10 years, the purchase price along with final pension installment is paid back to the beneficiary."}
        ]
    },
    "jal-jeevan-mission": {
        "fullname": "Jal Jeevan Mission (JJM) - Har Ghar Jal",
        "portal": "https://jaljeevanmission.gov.in",
        "benefit": "Ensures supply of 55 liters of safe drinking water per person per day through Functional Household Tap Connections (FHTC) to all rural households across India.",
        "eligibility": [
            "All households situated in rural villages, hamlets, and rural settlements.",
            "Special focus on water-scarce areas, drought-prone villages, and quality-affected habitations.",
            "Implemented through community participation, involving local Pani Samitis."
        ],
        "faqs": [
            {"q": "What is the main objective of Jal Jeevan Mission?", "a": "The main objective is to provide a functional tap water connection to every rural household in India, ensuring safe and sustainable drinking water supply."},
            {"q": "What is Har Ghar Jal certification?", "a": "A village is certified as 'Har Ghar Jal' when every household, school, Anganwadi centre, and community building has access to running tap water, verified by the Gram Sabha."},
            {"q": "Who tests the water quality under JJM?", "a": "Water quality is tested regularly using field test kits by local women trained in water testing, and samples are validated at government district water laboratories."}
        ]
    },
    "pm-gram-sadak": {
        "fullname": "Pradhan Mantri Gram Sadak Yojana (PMGSY)",
        "portal": "https://pmgsy.nic.in",
        "benefit": "Provides all-weather road connectivity to unconnected habitations in rural areas, improving access to markets, schools, health facilities, and urban centers.",
        "eligibility": [
            "Unconnected rural habitations with a population of 500+ in plains.",
            "Habitations with a population of 250+ in hill states, tribal areas, and desert areas.",
            "Administered by the Ministry of Rural Development, Government of India."
        ],
        "faqs": [
            {"q": "What is an all-weather road?", "a": "An all-weather road is one that is trafficable throughout the year, featuring proper cross-drainage structures and a bituminous/concrete surface."},
            {"q": "How are PMGSY roads maintained?", "a": "Road contractors are mandated to provide a 5-year routine maintenance contract, and subsequent maintenance is funded by state governments using dedicated state road funds."},
            {"q": "What is the PMGSY-III phase?", "a": "PMGSY-III aims to consolidate 1,25,000 km of existing major rural links and routes connecting habitations to agricultural markets, high schools, and hospitals."}
        ]
    },
    "rurban-mission": {
        "fullname": "Shyama Prasad Mukherji Rurban Mission (SPMRM)",
        "portal": "https://rurban.gov.in",
        "benefit": "Aims to develop 300 rural clusters (Rurban clusters) across India, providing them with urban-like infrastructure, skills training, economic activities, and basic services to stop migration.",
        "eligibility": [
            "Rural clusters with a population of 25,000 to 50,000 in plains.",
            "Clusters with a population of 5,000 to 15,000 in desert, hilly, or tribal areas.",
            "Clusters are selected based on economic growth potential, tourism, or industrial focus."
        ],
        "faqs": [
            {"q": "What facilities are provided under the Rurban Mission?", "a": "Facilities include 24/7 piped water supply, sanitation systems, solid & liquid waste management, street lights, local transport, skill development centers, and healthcare units."},
            {"q": "Who funds the Rurban Mission?", "a": "Funding is provided through a combination of state/central scheme convergence and Critical Gap Funding (CGF) up to 30% of the project cost from the Ministry of Rural Development."},
            {"q": "How does the mission stimulate economic growth?", "a": "By establishing agro-processing units, local warehouses, cold storages, tourism infrastructure, and digital CSC hubs in the cluster center."}
        ]
    },
    "ujala-scheme": {
        "fullname": "Unnat Jyoti by Affordable LEDs for All (UJALA)",
        "portal": "http://www.ujala.gov.in",
        "benefit": "Provides high-quality LED bulbs, LED tube lights, and energy-efficient 5-star rated fans at 50% of the market retail price to reduce household electricity bills and carbon emissions.",
        "eligibility": [
            "Every domestic household with an active electricity connection from a local distribution company (DISCOM).",
            "Can purchase up to a specified number of LED bulbs and fans by showing their electricity bill.",
            "Available through designated distribution kiosks in every district."
        ],
        "faqs": [
            {"q": "What is the warranty on UJALA LED bulbs?", "a": "UJALA LED bulbs come with a 3-year free replacement warranty for any technical defects, which can be claimed at any official distribution kiosk."},
            {"q": "Who implements the UJALA scheme?", "a": "The scheme is implemented by Energy Efficiency Services Limited (EESL), a joint venture of public sector undertakings under the Ministry of Power."},
            {"q": "How much electricity can I save using LED bulbs?", "a": "Replacing traditional 60W incandescent bulbs with UJALA 9W LED bulbs reduces lighting electricity consumption by up to 85%."}
        ]
    },
    "national-solar-mission": {
        "fullname": "Jawaharlal Nehru National Solar Mission (JNNSM)",
        "portal": "https://mnre.gov.in",
        "benefit": "Promotes solar energy generation through setting up mega solar parks, grid-connected solar power projects, and off-grid solar utilities with substantial central capital subsidies.",
        "eligibility": [
            "Solar power developers, government departments, public sector undertakings, and agricultural agencies.",
            "Individual farmers and institutions applying under specific component initiatives (like PM-KUSUM).",
            "Coordinated by the Ministry of New and Renewable Energy (MNRE)."
        ],
        "faqs": [
            {"q": "What is the target capacity of the National Solar Mission?", "a": "The mission originally targeted 20,000 MW which was later revised to 100 GW of solar power capacity, including grid-connected projects and rooftop solar panels."},
            {"q": "Is there a subsidy for solar developers?", "a": "Yes, Viability Gap Funding (VGF) and capital subsidies are provided to selected developers based on competitive bidding guidelines."},
            {"q": "How does it support rural farmers?", "a": "Under KUSUM, farmers are supported to install solar water pumps and set up small solar plants up to 2 MW on fallow lands to sell power back to the grid."}
        ]
    },
    "smart-cities": {
        "fullname": "Smart Cities Mission",
        "portal": "https://smartcities.gov.in",
        "benefit": "Aims to develop 100 selected cities as smart cities, upgrading their physical infrastructure, public transport, smart governance, waste management, and digital services.",
        "eligibility": [
            "Selected municipal corporations and city administrations in the 100 designated Smart Cities.",
            "Projects are implemented through a Special Purpose Vehicle (SPV) created for each city.",
            "Co-funded equally by the Central Government and respective State Governments."
        ],
        "faqs": [
            {"q": "How are cities selected under the Smart Cities Mission?", "a": "Cities were selected through a national competition called the 'Smart Cities Challenge', based on proposals for area development and smart solutions."},
            {"q": "What is an SPV in Smart Cities?", "a": "A Special Purpose Vehicle (SPV) is a public limited company formed at the city level, headed by a CEO, to plan, appraise, release funds, and implement smart city projects."},
            {"q": "What are some core components of a Smart City?", "a": "Core components include smart water meters, solid waste management, intelligent traffic management systems, integrated command centers, CCTV networks, and pedestrian-friendly streets."}
        ]
    },
    "amrut": {
        "fullname": "Atal Mission for Rejuvenation and Urban Transformation (AMRUT)",
        "portal": "https://amrut.gov.in",
        "benefit": "Ensures that every household in 500 selected cities has access to a tap with assured water supply, robust sewerage connections, stormwater drains, and green parks.",
        "eligibility": [
            "Municipal administrations and households in 500 selected cities and towns across India.",
            "Covers cities with a population of 100,000+ and all capital cities.",
            "Administered by the Ministry of Housing and Urban Affairs."
        ],
        "faqs": [
            {"q": "What is the primary focus of the AMRUT scheme?", "a": "The primary focus is to build basic infrastructure for water supply, sewerage, drainage, and urban green spaces in selected cities."},
            {"q": "What is AMRUT 2.0?", "a": "AMRUT 2.0 aims to make all cities 'water secure' by extending tap water connections to all households in all statutory towns, and focusing on recycling treated wastewater."},
            {"q": "Who monitors the implementation of projects?", "a": "Implementation is monitored by state-level high-powered steering committees, with third-party quality review audits."}
        ]
    },
    "gati-shakti": {
        "fullname": "PM Gati Shakti National Master Plan",
        "portal": "https://gatishakti.gov.in",
        "benefit": "A digital platform bringing 16 ministries (including Railways and Roadways) together for integrated planning and coordinated implementation of national infrastructure connectivity projects.",
        "eligibility": [
            "National infrastructure development agencies, state departments, and logistics entities.",
            "Designed to improve ease of doing business and reduce logistics costs in India from 14% of GDP to around 8%.",
            "Coordinated by the Department for Promotion of Industry and Internal Trade (DPIIT)."
        ],
        "faqs": [
            {"q": "What is the PM Gati Shakti National Master Plan?", "a": "It is a GIS-based digital platform that integrates spatial planning data of all infrastructure projects across ministries to ensure synchronized development."},
            {"q": "What are the 7 engines of Gati Shakti?", "a": "The seven engines driving the plan are Roads, Railways, Airports, Ports, Mass Transport, Waterways, and Logistics Infrastructure."},
            {"q": "How does Gati Shakti benefit the economy?", "a": "By eliminating departmental silos, preventing repeated road cuttings for cables/pipes, reducing project delays, and creating a unified national transport network."}
        ]
    },
    "national-food-security": {
        "fullname": "National Food Security Act (NFSA)",
        "portal": "https://nfsa.gov.in",
        "benefit": "Provides highly subsidized foodgrains to up to 75% of the rural and 50% of the urban population. Beneficiaries receive 5 kg of foodgrains per person per month at ₹3/kg (rice) and ₹2/kg (wheat).",
        "eligibility": [
            "Priority households (PHH) and Antyodaya Anna Yojana (AAY) households.",
            "Identified by state governments based on rural/urban poverty criteria.",
            "Must possess an active Ration Card linked with Aadhaar."
        ],
        "faqs": [
            {"q": "What are the foodgrain quotas under NFSA?", "a": "Priority Households (PHH) receive 5 kg per person per month, while Antyodaya Anna Yojana (AAY) households (the poorest of the poor) receive 35 kg per family per month."},
            {"q": "What is the One Nation One Ration Card (ONORC)?", "a": "ONORC is a national portability system allowing migratory beneficiaries to claim their subsidized foodgrains from any Fair Price Shop across India using biometric authentication."},
            {"q": "Are foodgrains currently free under NFSA?", "a": "Yes, under the Pradhan Mantri Garib Kalyan Anna Yojana (PMGKAY), the government has made the NFSA foodgrain allocation completely free of charge for all eligible beneficiaries."}
        ]
    },
    "soil-health-card": {
        "fullname": "Soil Health Card Scheme",
        "portal": "https://soilhealth.dac.gov.in",
        "benefit": "Provides farmers with a detailed printed card showing 12 soil parameters (N, P, K, pH, etc.) and crop-wise recommendations of organic manure and chemical fertilizers needed for their farms.",
        "eligibility": [
            "All farmers across India who own cultivable land holdings.",
            "Soil samples are collected by agricultural department representatives every 3 years.",
            "Issued completely free of cost to the landowning farmers."
        ],
        "faqs": [
            {"q": "What parameters are tested under the Soil Health Card?", "a": "It tests 12 parameters: Macro-nutrients (Nitrogen, Phosphorus, Potassium), Secondary nutrients (Sulfur), Micro-nutrients (Zinc, Iron, Copper, Manganese, Boron), and Physical parameters (pH, EC, Organic Carbon)."},
            {"q": "How often is the Soil Health Card updated?", "a": "The cards are updated and re-issued to farmers once every 3 years after fresh soil sample collections from their fields."},
            {"q": "How does it help farmers?", "a": "It prevents overuse of chemical fertilizers like Urea, reduces cost of cultivation, and increases crop yields by recommending exact nutrient dosages."}
        ]
    },
    "paramparagat-krishi": {
        "fullname": "Paramparagat Krishi Vikas Yojana (PKVY)",
        "portal": "https://dackvk.nic.in",
        "benefit": "Promotes organic farming through cluster approach. Farmers receive ₹50,000 per hectare financial assistance for 3 years, with 62% (₹31,000) directly paid for organic inputs and seeds.",
        "eligibility": [
            "Individual farmers owning cultivable lands who form a cluster.",
            "Every cluster must have a minimum of 50 farmers occupying 50 acres of land.",
            "Special focus on hilly, tribal, and rainfed agricultural regions."
        ],
        "faqs": [
            {"q": "What certification is used under the PKVY scheme?", "a": "Participatory Guarantee System (PGS) India certification is used, which is a peer-review organic certification process for farmer groups."},
            {"q": "How is the financial aid disbursed?", "a": "The financial aid of ₹50,000 per hectare is paid directly to the farmers' bank accounts via DBT in installments over a 3-year organic conversion period."},
            {"q": "What inputs are subsidized under PKVY?", "a": "Subsidies are provided for purchasing organic seeds, bio-fertilizers, bio-pesticides, vermicompost, and organic botanical extracts."}
        ]
    },
    "pm-jan-aushadhi": {
        "fullname": "Pradhan Mantri Bhartiya Janaushadhi Pariyojana (PMBJP)",
        "portal": "http://janaushadhi.gov.in",
        "benefit": "Provides quality generic medicines, surgical items, and medical consumables at prices 50% to 90% cheaper than equivalent branded medicines in the market.",
        "eligibility": [
            "All citizens of India can buy medicines from Jan Aushadhi Kendras without restrictions.",
            "Doctors are encouraged to prescribe generic names instead of branded formulations.",
            "Individuals/NGOs can apply to open a Jan Aushadhi Kendra and receive up to ₹5 lakh government incentives."
        ],
        "faqs": [
            {"q": "Are generic medicines as safe as branded ones?", "a": "Yes. PMBJP generic medicines are procured only from WHO-GMP certified manufacturers and are tested at NABL accredited labs to ensure therapeutic efficacy."},
            {"q": "Who manages the PMBJP scheme?", "a": "The scheme is managed by the Pharmaceuticals and Medical Devices Bureau of India (PMBI) under the Department of Pharmaceuticals, Ministry of Chemicals and Fertilizers."},
            {"q": "How can I find a Jan Aushadhi Kendra near me?", "a": "You can find local stores using the 'Jan Aushadhi Sugam' mobile application or by visiting the official PMBJP portal store locator."}
        ]
    },
    "mission-indradhanush": {
        "fullname": "Mission Indradhanush (Universal Immunization)",
        "portal": "https://www.nhm.gov.in",
        "benefit": "Aims to fully immunize children under 2 years of age and pregnant women against 12 vaccine-preventable diseases including Polio, Tetanus, Measles, Hepatitis B, and TB.",
        "eligibility": [
            "Children under the age of 2 years who have missed or are partially covered under routine immunization.",
            "All pregnant women requiring Tetanus and Diphtheria (Td) vaccines.",
            "Offered completely free of charge at all government primary health centers and immunization camps."
        ],
        "faqs": [
            {"q": "What diseases are covered under Mission Indradhanush?", "a": "It provides vaccines against 12 life-threatening diseases: Diphtheria, Whooping cough, Tetanus, Polio, Tuberculosis, Measles, Hepatitis B, Meningitis, Pneumonia, Rotavirus, Rubella, and Japanese Encephalitis."},
            {"q": "What is Intensified Mission Indradhanush (IMI)?", "a": "IMI is a special high-intensity campaign targeting hard-to-reach districts, urban slums, and tribal blocks with low routine immunization coverage."},
            {"q": "Where can I get my child vaccinated under this scheme?", "a": "Vaccinations are available free of charge at all Government sub-centers, Primary Health Centers (PHCs), Community Health Centers (CHCs), and government hospitals."}
        ]
    },
    "janani-suraksha": {
        "fullname": "Janani Suraksha Yojana (JSY)",
        "portal": "https://www.nhm.gov.in",
        "benefit": "A safe motherhood intervention scheme providing a cash incentive up to ₹1,400 to rural pregnant women and ₹1,000 to urban pregnant women for delivering in public health institutions.",
        "eligibility": [
            "All pregnant women delivering in government health facilities or accredited private hospitals.",
            "Special focus on Low Performing States (LPS) where all pregnant women are eligible regardless of age or number of children.",
            "Asha workers also receive cash incentives for facilitating institutional deliveries."
        ],
        "faqs": [
            {"q": "What is the cash benefit for rural mothers in LPS?", "a": "Rural pregnant women in Low Performing States (LPS) receive ₹1,400, while urban mothers receive ₹1,000 upon institutional delivery in government facilities."},
            {"q": "How is the JSY cash payment made?", "a": "The payment is directly credited to the bank account of the beneficiary mother through DBT, usually before discharge from the hospital."},
            {"q": "Who is eligible in High Performing States?", "a": "In High Performing States, the cash benefit is limited to BPL/SC/ST pregnant women aged 19 years and above, up to their first two live births."}
        ]
    },
    "jssk": {
        "fullname": "Janani Shishu Suraksha Karyakram (JSSK)",
        "portal": "https://www.nhm.gov.in",
        "benefit": "Entitles all pregnant women delivering in public health institutions to completely free and cashless deliveries (including C-sections), free drugs, diagnostics, diet, and free transport from home and back.",
        "eligibility": [
            "All pregnant women delivering at any government public health facility.",
            "Sick infants (up to 1 year of age) accessing public health institutions for treatment.",
            "Includes all diagnostic tests, operations, medicines, and consumables."
        ],
        "faqs": [
            {"q": "Are caesarean sections free under JSSK?", "a": "Yes, both normal deliveries and Caesarean sections are provided completely free of charge, including all consumables, drugs, and blood transfusions if required."},
            {"q": "What transport facilities are provided?", "a": "JSSK provides free transport from home to health facility, inter-facility transfer in case of referral, and free drop back from health facility to home after 48 hours of delivery."},
            {"q": "Is there any charge for diagnostics or blood?", "a": "No, all diagnostic tests (ultrasound, urine/blood tests) and provision of blood are completely free of charge under the JSSK guidelines."}
        ]
    },
    "saubhagya": {
        "fullname": "Pradhan Mantri Sahaj Bijli Har Ghar Yojana (Saubhagya)",
        "portal": "https://saubhagya.gov.in",
        "benefit": "Provides free electricity connections to all willing un-electrified households in rural areas and all poor households in urban areas across the country.",
        "eligibility": [
            "All households in rural areas without electricity connections.",
            "Urban households belonging to economically weaker sections (EWS) or BPL categories.",
            "Beneficiaries are identified using SECC 2011 data; others can get a connection by paying ₹500 in 10 installments."
        ],
        "faqs": [
            {"q": "Is the monthly electricity consumption free under Saubhagya?", "a": "No. The scheme only covers the cost of releasing the electricity connection (meter, service cable, and basic wiring). Households must pay for their actual monthly electricity usage based on tariff rates."},
            {"q": "What is provided to un-electrified remote households?", "a": "For households in remote/inaccessible areas where grid extension is not feasible, the scheme provides Solar Standalone Power packs containing a 200 to 300 Wp solar panel, battery, 5 LED lights, 1 fan, and 1 power plug."},
            {"q": "Who implements the Saubhagya scheme?", "a": "Rural Electrification Corporation (REC) is the nodal agency, coordinating with state electricity distribution companies (DISCOMs) for ground-level execution."}
        ]
    },
    "samagra-shiksha": {
        "fullname": "Samagra Shiksha - Integrated Scheme for School Education",
        "portal": "https://samagra.education.gov.in",
        "benefit": "An integrated program for school education from pre-school to class 12, providing funds to schools for smart classrooms, digital boards, science labs, libraries, free textbooks, and teacher training.",
        "eligibility": [
            "All government and government-aided schools across all states and Union Territories.",
            "Benefits students enrolled in primary, upper primary, secondary, and senior secondary schools.",
            "Administered by the Department of School Education and Literacy, Ministry of Education."
        ],
        "faqs": [
            {"q": "What schemes were merged into Samagra Shiksha?", "a": "Three major school education schemes were merged: Sarva Shiksha Abhiyan (SSA), Rashtriya Madhyamik Shiksha Abhiyan (RMSA), and Teacher Education (TE)."},
            {"q": "How does the scheme promote girl education?", "a": "It funds the setting up of Kasturba Gandhi Balika Vidyalayas (KGBVs), which are residential schools for girls from disadvantaged categories (SC/ST/OBC/Minority/BPL) in educationally backward blocks."},
            {"q": "Is vocational education supported?", "a": "Yes, the scheme provides financial support for integrating vocational education with academic streams in classes 9 to 12, as highlighted in NEP 2020."}
        ]
    },
    "pm-shri-schools": {
        "fullname": "PM Schools for Rising India (PM SHRI)",
        "portal": "https://pmshrischools.education.gov.in",
        "benefit": "Upgrades and develops more than 14,500 schools across India as model schools that showcase all components of the National Education Policy (NEP) 2020, featuring smart classrooms, green infrastructure, and skill labs.",
        "eligibility": [
            "Existing government schools (Central, State, or Local bodies) selected through a 3-stage challenge process.",
            "Selected schools must have playground facilities, boundary walls, and high student enrollment ratios.",
            "Co-funded by the Central Government and respective State Governments."
        ],
        "faqs": [
            {"q": "What are PM SHRI schools?", "a": "PM SHRI schools are model schools designed to deliver high-quality education in a safe, stimulating learning environment, showcasing modern pedagogy, green school campuses, and vocational training."},
            {"q": "How are schools selected for PM SHRI?", "a": "Schools apply online and are evaluated on parameters like infrastructure, physical assets, student-teacher ratio, and green initiatives in a competitive challenge format."},
            {"q": "What is the green school concept in PM SHRI?", "a": "Green schools incorporate solar panels, LED lights, water harvesting systems, organic gardens, waste recycling, and plastic-free campuses to teach eco-friendly living."}
        ]
    },
    "pmrf": {
        "fullname": "Prime Minister's Research Fellowship (PMRF)",
        "portal": "https://pmrf.in",
        "benefit": "Provides a monthly fellowship of ₹70,000 to ₹80,000 and an annual research contingency grant of ₹2 Lakh for 5 years to doctoral (Ph.D.) students in IITs, IISc, IISERs, and top central universities.",
        "eligibility": [
            "Must be admitted to a Ph.D. program in one of the PMRF granting institutions (IITs, IISc, IISERs, NITs, Central Universities).",
            "Must have completed B.Tech/M.Tech/M.Sc. with a minimum CGPA of 8.0 or equivalent, and a valid GATE score.",
            "Selected through a rigorous evaluation of research project proposals."
        ],
        "faqs": [
            {"q": "What is the monthly fellowship amount under PMRF?", "a": "The fellowship is ₹70,000/month for Year 1 & 2, ₹75,000/month for Year 3, and ₹80,000/month for Year 4 & 5, along with a ₹2 Lakh annual research grant."},
            {"q": "Can direct entry Ph.D. students apply?", "a": "Yes, direct entry students (immediately after B.Tech/B.S.) as well as lateral entry students (already enrolled in Ph.D. for 1-2 semesters) can apply for the fellowship."},
            {"q": "Who evaluates PMRF applications?", "a": "Applications are reviewed by national subject expert committees, assessing research potential, academic records, and the quality of the Ph.D. project proposal."}
        ]
    },
    "national-overseas-scholarship": {
        "fullname": "National Overseas Scholarship Scheme (NOS)",
        "portal": "https://nosmsje.gov.in",
        "benefit": "Provides complete financial assistance including tuition fees, annual maintenance allowance (USD 15,400 in US, GBP 9,900 in UK), visa fees, and return airfare to selected students pursuing Master's or Ph.D. abroad.",
        "eligibility": [
            "Belonging to Scheduled Castes (SC), Denotified/Nomadic Tribes, or Landless Agricultural Laborers' families.",
            "Family income must not exceed ₹8,000,000 per annum.",
            "Candidate must have secured at least 60% marks in their graduation/post-graduation and be under 35 years of age."
        ],
        "faqs": [
            {"q": "How many scholarships are awarded annually under NOS?", "a": "The Ministry of Social Justice and Empowerment awards 125 slots annually to eligible students for pursuing higher education abroad."},
            {"q": "Is tuition fee paid directly to the foreign university?", "a": "Yes, the actual tuition fee is paid directly by the Indian mission in that country to the foreign university, while maintenance allowance is paid to the student's bank account."},
            {"q": "Can I study any course under the NOS scheme?", "a": "Scholarships are available for a wide range of subjects in Science, Engineering, Medicine, Social Sciences, and Humanities, at foreign universities ranked in the top 500 QS rankings."}
        ]
    },
    "pragati-scholarship": {
        "fullname": "AICTE Pragati Scholarship Scheme for Girl Students",
        "portal": "https://www.aicte-india.org",
        "benefit": "Provides a scholarship of ₹50,000 per annum to eligible girl students to cover tuition fees, books, equipment, laptops, and hostel expenses while pursuing technical degree or diploma courses.",
        "eligibility": [
            "Girl students admitted to the 1st year of a technical degree/diploma course in an AICTE approved institution.",
            "Maximum of two girls per family are eligible.",
            "Family income from all sources must be less than ₹8,000,000 per annum."
        ],
        "faqs": [
            {"q": "How many Pragati scholarships are given every year?", "a": "AICTE awards 5,000 scholarships for Degree courses and 5,000 scholarships for Diploma courses annually to girl students across India."},
            {"q": "How is the Pragati scholarship money paid?", "a": "The scholarship amount of ₹50,000 is directly credited to the girl student's Aadhaar-seeded bank account through DBT once a year."},
            {"q": "Is the scholarship renewable?", "a": "Yes, it is renewable for subsequent years of study (up to 4 years for degree, 3 years for diploma) based on passing exams with good academic performance."}
        ]
    },
    "mission-shakti": {
        "fullname": "Mission Shakti - Women Safety & Empowerment",
        "portal": "https://wcd.nic.in",
        "benefit": "An integrated program for women safety, security, and empowerment. Comprises sub-schemes 'Sambal' (One Stop Centres, 181 helpline, Beti Bachao) and 'Samarthya' (Pradhan Mantri Matru Vandana Yojana, working women hostels).",
        "eligibility": [
            "All women and girls who require protection, rescue, counseling, or temporary shelter.",
            "Pregnant and lactating mothers for maternity benefits under Matru Vandana Yojana.",
            "Administered by the Ministry of Women and Child Development."
        ],
        "faqs": [
            {"q": "What is the 'Sambal' component in Mission Shakti?", "a": "'Sambal' focuses on safety and security of women, coordinating One Stop Centres (OSC), Women Helplines (181), Beti Bachao Beti Padhao, and Nari Adalats."},
            {"q": "What is the 'Samarthya' component?", "a": "'Samarthya' focuses on socio-economic empowerment of women, including working women hostels, day care creches, and Pradhan Mantri Matru Vandana Yojana (PMMVY) cash incentives."},
            {"q": "Who manages the One Stop Centres?", "a": "One Stop Centres are managed at the district level, providing integrated support like medical aid, legal counseling, temporary shelter, and police help under one roof."}
        ]
    },
    "mahila-shakti-kendra": {
        "fullname": "Mahila Shakti Kendra (MSK) Scheme",
        "portal": "https://wcd.nic.in",
        "benefit": "Empowers rural women with opportunities for skill development, digital literacy, employment, and health awareness through community mobilization and student volunteers.",
        "eligibility": [
            "Rural women requiring vocational training, digital education, or access to government schemes.",
            "Implemented through block-level and district-level support centers.",
            "Utilizes student volunteers to sensitize rural communities on women rights."
        ],
        "faqs": [
            {"q": "What is the role of student volunteers in MSK?", "a": "College student volunteers are deployed in rural blocks to raise awareness about government welfare schemes, digital banking, and health initiatives among rural women."},
            {"q": "How is the MSK scheme funded?", "a": "It is a centrally sponsored scheme funded on a 60:40 ratio between the Centre and States (90:10 for North Eastern and Himalayan states)."},
            {"q": "What are District Level Centres for Women (DLCW)?", "a": "DLCW under MSK serve as hubs for coordinating women-centric schemes, providing local support, and maintaining databases of welfare beneficiaries at the district level."}
        ]
    },
    "cgtmse-scheme": {
        "fullname": "Credit Guarantee Fund Trust for Micro and Small Enterprises (CGTMSE)",
        "portal": "https://www.cgtmse.in",
        "benefit": "Provides credit guarantees to financial institutions, allowing micro and small enterprises to obtain collateral-free business loans up to ₹5 Crore from banks, SIDBI, and NBFCs.",
        "eligibility": [
            "New and existing Micro and Small Enterprises (MSEs) engaged in manufacturing or service activities.",
            "Retail trade and select educational institutions are also covered under revised rules.",
            "The borrowing unit must satisfy MSME classification criteria."
        ],
        "faqs": [
            {"q": "What is the maximum loan limit under CGTMSE?", "a": "The credit guarantee limit has been increased up to ₹5 Crore per eligible borrower, allowing banks to extend collateral-free loans up to this limit."},
            {"q": "What is the guarantee coverage percentage?", "a": "The guarantee coverage ranges from 75% to 85% of the loan amount, with special 85% coverage for micro enterprises, women-owned businesses, and units in North-East India."},
            {"q": "How does a business apply for CGTMSE?", "a": "Businesses do not apply to CGTMSE directly. You must apply for a business loan at any member bank or financial institution, which will then process the CGTMSE cover for your loan if eligible."}
        ]
    },
    "national-career-service": {
        "fullname": "National Career Service (NCS) Portal",
        "portal": "https://www.ncs.gov.in",
        "benefit": "A digital job matching platform connecting job seekers with active employers, providing career counseling, vocational guidance, skills training info, and local work opportunities.",
        "eligibility": [
            "All Indian citizens seeking employment, career guidance, or skills training.",
            "Employers seeking to post vacancies and hire local talent.",
            "Registration is completely free of charge for both job seekers and employers."
        ],
        "faqs": [
            {"q": "What is the NCS portal?", "a": "NCS is a national digital portal developed by the Ministry of Labour and Employment that offers job matching, career counseling, vocational training details, and job fair schedules."},
            {"q": "Does NCS offer any career counseling?", "a": "Yes, the portal lists certified career counselors and has dedicated Model Career Centres (MCCs) in districts providing offline guidance and aptitude tests."},
            {"q": "Can I link my NCS account with Aadhaar?", "a": "Yes, linking with Aadhaar or Shramik ID is recommended during registration to verify credentials and ensure trust for employers."}
        ]
    },
    "national-apprenticeship": {
        "fullname": "National Apprenticeship Promotion Scheme (NAPS)",
        "portal": "https://www.apprenticeshipindia.gov.in",
        "benefit": "Promotes apprenticeship training in industries. The government shares 25% of the prescribed monthly stipend (up to a maximum of ₹1,500 per month per apprentice) paid to candidates.",
        "eligibility": [
            "Candidates who are at least 15 years of age and have completed Class 5/8/10/12, ITI, or Diploma.",
            "Employers must have registration on the national apprenticeship portal and satisfy minimum employee counts.",
            "Administered by the Ministry of Skill Development and Entrepreneurship."
        ],
        "faqs": [
            {"q": "What is the NAPS stipend benefit for apprentices?", "a": "Apprentices receive a monthly stipend as per industry standards, and the government reimburses 25% of it (up to ₹1,500/month) directly to the employer's account."},
            {"q": "What is the duration of apprenticeship training?", "a": "The duration ranges from 6 months to 2 years based on the specific trade or sector curriculum guidelines."},
            {"q": "Do candidates receive a certificate after training?", "a": "Yes, candidates receive a National Apprenticeship Certificate (NAC) issued by the National Council for Vocational Education and Training (NCVET) after passing trade assessments."}
        ]
    },
    "garib-kalyan-rojgar": {
        "fullname": "Garib Kalyan Rojgar Abhiyaan (GKRA)",
        "portal": "https://mrd.nic.in",
        "benefit": "A massive 125-day employment generation and infrastructure creation campaign for returnee migrant workers in 116 selected districts across 6 states during the Covid-19 pandemic.",
        "eligibility": [
            "Returnee migrant workers and rural households in the 116 designated districts.",
            "Covers selected rural districts in Bihar, Uttar Pradesh, Madhya Pradesh, Rajasthan, Odisha, and Jharkhand.",
            "Coordinated by the Ministry of Rural Development."
        ],
        "faqs": [
            {"q": "What works were executed under GKRA?", "a": "Works included constructing rural houses, laying optical fiber cables, building community sanitation complexes, farm ponds, well construction, and planting trees."},
            {"q": "How many ministries coordinated for GKRA?", "a": "A total of 12 ministries (including Rural Development, Panchayati Raj, Roadways, Railways, Telecom, and Mines) converged their schemes for this campaign."},
            {"q": "Was skill training provided?", "a": "Yes, Krishi Vigyan Kendras provided skill training and entrepreneurship guidance to returnee workers to help them find local livelihood options."}
        ]
    },
    "pmegp": {
        "fullname": "Prime Minister's Employment Generation Programme (PMEGP)",
        "portal": "https://www.kviconline.gov.in",
        "benefit": "A credit-linked subsidy scheme for setting up micro-enterprises. Offers capital subsidies of 15% to 35% on project costs up to ₹50 Lakh for manufacturing units and ₹20 Lakh for service units.",
        "eligibility": [
            "Any individual above 18 years of age with at least Class 8 education (for projects above ₹10 Lakh in manufacturing).",
            "Self Help Groups, Co-operative societies, and charitable trusts.",
            "Implemented by Khadi and Village Industries Commission (KVIC) at the national level."
        ],
        "faqs": [
            {"q": "What is the maximum subsidy under PMEGP?", "a": "The subsidy is 25% for general category and 35% for special categories (SC/ST/OBC/Women/Minorities) in rural areas, and 15% (general) / 25% (special) in urban areas."},
            {"q": "What is the maximum project limit under PMEGP?", "a": "The maximum project cost eligible for subsidy is ₹50 Lakh for manufacturing sector units and ₹20 Lakh for service/business sector units."},
            {"q": "What is the lock-in period for the subsidy?", "a": "The subsidy amount (margin money) is kept in a fixed deposit for 3 years at the financing bank and is adjusted against the loan account after successful verification."}
        ]
    },
    "stand-up-india": {
        "fullname": "Stand-Up India Scheme",
        "portal": "https://www.standupmitra.in",
        "benefit": "Facilitates bank loans between ₹10 Lakh and ₹1 Crore to at least one Scheduled Caste (SC) or Scheduled Tribe (ST) borrower and at least one Woman borrower per bank branch for setting up a greenfield enterprise.",
        "eligibility": [
            "SC/ST and/or women entrepreneurs above 18 years of age.",
            "The enterprise must be a greenfield project (first-time venture) in manufacturing, services, agri-allied, or trading sector.",
            "For non-individual enterprises, at least 51% shareholding must be held by an SC/ST or woman entrepreneur."
        ],
        "faqs": [
            {"q": "What is a greenfield enterprise under Stand-Up India?", "a": "A greenfield enterprise refers to the first-time venture of the beneficiary in manufacturing, services, trading, or agricultural allied activities."},
            {"q": "What is the loan repayment period?", "a": "The loan is repayable in 7 years with a maximum moratorium period of 18 months."},
            {"q": "How is the loan secured?", "a": "Loans are secured by primary security (hypothecation of assets) and can be backed by a collateral guarantee under the Credit Guarantee Scheme for Stand-Up India (CGSSI)."}
        ]
    }
}

def generate_page(s, schemes_list):
    # Determine category info
    cat_id = s["category"]
    cat_info = CURATED_CATEGORIES.get(cat_id)
    if not cat_info:
        # Fallback category details
        cat_info = {
            "name": cat_id.replace("&amp;", "&").capitalize(),
            "emoji": '<svg class="icon-svg" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M12 8v8M8 12h8"/></svg>',
            "class": f"tag-{cat_id}",
            "color": cat_id
        }

    # Fetch overrides if available
    override = SCHEME_FACTS.get(s["id"], {})
    fullname = override.get("fullname", s.get("fullname", s.get("title")))
    
    # 2026 Duplicate Check: Ensure we don't have double year tags!
    if "2026" not in fullname:
        fullname = f"{fullname} 2026"
    else:
        # Clean double instances if they crept in
        fullname = fullname.replace("2026 2026", "2026")
        
    portal = override.get("portal", "https://www.myscheme.gov.in")
    description = s.get("meta_desc", s.get("desc", ""))
    if not description:
        description = f"Complete guide to {fullname}. Learn about eligibility, benefits, application process, and documents required."
    
    # 1. Overview text
    if s["id"] in SCHEME_FACTS:
        overview_text = f"The <strong>{fullname}</strong> is a key developmental initiative launched by the Government of India. This scheme represents a major milestone designed specifically to address critical needs in the <strong>{cat_info['name']}</strong> sector. By providing a comprehensive support mechanism, the initiative aims to target eligible beneficiaries across all states and Union Territories, ensuring that the benefits of developmental growth reach the grass-roots level. Under the supervision of the respective nodal Ministry, the scheme is backed by a substantial budgetary allocation, reflecting the government's commitment to social welfare, economic empowerment, and national development. Through transparent implementation channels such as Direct Benefit Transfer (DBT), Aadhaar-linked verification, and digital application tracking, the program minimizes intermediaries and maximizes efficiency, making it one of the most trusted welfare initiatives in the country today."
    else:
        overview_text = s.get("intro", "")
        if not overview_text:
            overview_text = f"The <strong>{fullname}</strong> is an essential welfare program launched by the Government of India to support eligible beneficiaries in the <strong>{cat_info['name']}</strong> sector."

    # 2. Benefits text & Table
    if s["id"] in SCHEME_FACTS:
        benefits_text = override["benefit"]
        table_html = f"""<table>
          <thead>
            <tr>
              <th>Benefit Category</th>
              <th>Details &amp; Coverage</th>
              <th>Disbursal Mode</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Direct Support</td>
              <td>{override["benefit"]}</td>
              <td>Direct Benefit Transfer (DBT) / Direct Allocation</td>
            </tr>
            <tr>
              <td>Nodal Supervision</td>
              <td>Monitored under guidelines of the official portal: {override["portal"]}</td>
              <td>Bank Seeding / Nodal Kiosks</td>
            </tr>
          </tbody>
        </table>"""
    else:
        benefits_text = s.get("benefits_text", "")
        table_html = s.get("table_html", "")

    # 3. Eligibility Criteria list
    if s["id"] in SCHEME_FACTS:
        eligibility_list = override["eligibility"]
    else:
        eligibility_list = s.get("eligibility_list", [
            "Must be a permanent citizen of India.",
            f"Should belong to the target demographic defined for the {cat_info['name']} sector.",
            "Applicants must possess valid identity proofs, including Aadhaar card and functional bank account."
        ])
        
    eligibility_html = "<ul>\n" + "\n".join([f"              <li>{item}</li>" for item in eligibility_list]) + "\n            </ul>"

    # Exclusions
    exclusions_list = s.get("exclusions_list", [
        "Institutional landholders or corporate entities.",
        "Families with retired or serving government employees (except Group D/MTS staff).",
        "Income tax payers from the preceding financial assessment year."
    ])
    exclusions_html = "<ul>\n" + "\n".join([f"              <li>{item}</li>" for item in exclusions_list]) + "\n            </ul>"

    # 4. Documents Required list
    documents_list = s.get("documents_list", [
        "<strong>Aadhaar Card:</strong> Mandatory for biometric verification and identity mapping.",
        "<strong>Proof of Address:</strong> Voter ID, utility bills, or domicile certificate.",
        "<strong>Bank Account Passbook:</strong> Aadhaar-seeded bank account copy showing IFSC and account details."
    ])
    documents_html = "<ul>\n" + "\n".join([f"              <li>{item}</li>" for item in documents_list]) + "\n            </ul>"

    # 5. How to Apply steps
    if s["id"] in SCHEME_FACTS:
        apply_steps = [
            f"Visit the official portal designated for the scheme at <strong>{override['portal'].replace('https://', '').replace('http://', '')}</strong>.",
            "On the homepage, select the 'New Registration' or 'Apply Online' option.",
            "Fill in basic details including Aadhaar card number, mobile number, and select your state/district.",
            "Verify your mobile number using the One-Time Password (OTP) received.",
            "Complete the comprehensive application form by entering personal details, bank information, and family declaration.",
            "Upload scanned copies of all required documents in the prescribed format (PDF/JPEG).",
            "Review the entered details carefully to avoid rejection, then click on the 'Submit' button.",
            "Save or print the generated Application Reference Number for tracking your status."
        ]
    else:
        apply_steps = s.get("apply_steps", [
            "Navigate to the official portal designated for the scheme or visit the national myScheme portal.",
            "On the homepage, select the 'New Registration' or 'Apply Online' option.",
            "Fill in basic details including Aadhaar card number, mobile number, and select your state/district.",
            "Verify your mobile number using the One-Time Password (OTP) received.",
            "Complete the comprehensive application form by entering personal details, bank information, and family declaration.",
            "Upload scanned copies of all required documents.",
            "Review the entered details carefully to avoid rejection, then click on the 'Submit' button.",
            "Save or print the generated Application Reference Number."
        ])
    apply_html = "<ol>\n" + "\n".join([f"              <li>{item}</li>" for item in apply_steps]) + "\n            </ol>"

    # 6. Status Check steps
    if s["id"] in SCHEME_FACTS:
        status_steps = [
            f"Go to the official portal at <strong>{override['portal'].replace('https://', '').replace('http://', '')}</strong>.",
            "Click on the 'Know Your Status' or 'Beneficiary Status' tab on the homepage.",
            "Select your search parameter: Application Reference Number, Mobile Number, or Aadhaar Card Number.",
            "Enter the required number and fill in the security captcha code.",
            "Click on 'Get Data' or 'Check Status' to display your application approval stage and payment status."
        ]
    else:
        status_steps = s.get("status_steps", [
            "Go to the official portal designated for the scheme.",
            "Click on the 'Know Your Status' or 'Beneficiary Status' tab on the homepage.",
            "Select your search parameter: Application Reference Number, Mobile Number, or Aadhaar Card Number.",
            "Enter the required and click check status."
        ])
    status_html = "<ol>\n" + "\n".join([f"              <li>{item}</li>" for item in status_steps]) + "\n            </ol>"

    # 7. FAQs
    if s["id"] in SCHEME_FACTS:
        faqs_list = override["faqs"]
    else:
        faqs_list = s.get("faqs", [
            {"q": f"Who is the nodal ministry for {s['title']}?", "a": f"The scheme is administered and funded by the Central Government through its respective nodal ministry, coordinating with state departments for local verification and distribution."},
            {"q": "Is Aadhaar card mandatory to avail benefits?", "a": "Yes, Aadhaar card is mandatory for identity verification and bank account seeding, which is required to receive Direct Benefit Transfer (DBT) payments."}
        ])
        
    faq_html = '            <div class="faq-accordion">\n'
    for faq in faqs_list:
        faq_html += f"""              <div class="faq-item">
                <h3 class="faq-question">{faq["q"]}</h3>
                <div class="faq-answer">
                  <p>{faq["a"]}</p>
                </div>
              </div>\n"""
    faq_html += "            </div>\n"

    # Table of Contents
    toc_html = """            <div class="toc">
              <h4>Table of Contents</h4>
              <ol>
                <li><a href="#overview">Scheme Overview</a></li>
                <li><a href="#benefits">Benefits &amp; Financial Assistance</a></li>
                <li><a href="#eligibility">Eligibility Criteria</a></li>
                <li><a href="#documents">Documents Required</a></li>
                <li><a href="#apply">How to Apply</a></li>
                <li><a href="#status">Status Check</a></li>
                <li><a href="#faq">Frequently Asked Questions</a></li>
              </ol>
            </div>"""

    # Generate Dynamic Related Links (keep only 2 schemes in the same category)
    related_schemes = [x for x in schemes_list if x["category"] == cat_id and x["id"] != s["id"]][:2]
    related_links_html = ""
    for r in related_schemes:
        related_links_html += f'              <li><a href="{r["id"]}">{r["title"]}</a></li>\n'

    # E-E-A-T Editorial Card Widget (No unverifiable synthetic named expert, uses editorial board branding)
    author_card = """          <!-- E-E-A-T Author Card -->
          <div class="sidebar-widget author-widget" style="background: linear-gradient(135deg, rgba(255,107,0,0.05) 0%, rgba(255,107,0,0.02) 100%); border: 1px solid rgba(255,107,0,0.15); border-radius: 12px; padding: 1.25rem;">
            <h4 style="color: var(--accent-orange); font-size: 0.95rem; margin-top: 0; margin-bottom: 0.75rem; text-transform: uppercase; letter-spacing: 0.05em; border-bottom: none; padding-bottom: 0;">Fact Checked &amp; Verified</h4>
            <div class="author-info" style="display: flex; gap: 0.75rem; align-items: flex-start; margin-bottom: 0.75rem;">
              <div class="author-avatar-container" style="position: relative; width: 44px; height: 44px; border-radius: 50%; overflow: hidden; border: 2px solid var(--accent-orange); box-shadow: var(--shadow-small); display: flex; align-items: center; justify-content: center; background: var(--off-white); flex-shrink: 0;">
                <img src="profile.png" alt="Durga Sravan Challagolla" style="width: 100%; height: 100%; object-fit: cover; display: block;" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
                <div class="author-avatar-fallback" style="width: 100%; height: 100%; font-size: 1.05rem; display: none; align-items: center; justify-content: center; background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%); color: var(--white); font-weight: bold;">DS</div>
              </div>
              <div>
                <h5 style="margin: 0 0 0.15rem; font-size: 0.95rem; color: var(--text-main); font-family: var(--font-header);">Durga Sravan Challagolla</h5>
                <p style="margin: 0; font-size: 0.75rem; color: var(--text-secondary); line-height: 1.2;">Founder, Owner &amp; Lead Reviewer</p>
              </div>
            </div>
            <p style="margin: 0 0 0.75rem 0; font-size: 0.8rem; color: var(--text-secondary); line-height: 1.45;">Site founder and manager. Durga reviews all policies against official gazette releases and government portals to ensure accurate, verified info.</p>
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.5rem;">
              <div class="editorial-badge" style="display: inline-flex; align-items: center; gap: 0.35rem; font-size: 0.72rem; color: #15803d; font-weight: 600; background: #f0fdf4; padding: 0.25rem 0.5rem; border-radius: 4px; border: 1px solid #bbf7d0; width: fit-content;">
                <svg viewBox="0 0 24 24" style="width: 12px; height: 12px; fill: none; stroke: currentColor; stroke-width: 3;" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
                Verified Owner &amp; Author
              </div>
              <a href="https://www.linkedin.com/in/durga-sravan-challagolla-67693a377/" target="_blank" rel="noopener noreferrer" style="display: inline-flex; align-items: center; gap: 0.25rem; color: #0077b5; font-size: 0.75rem; text-decoration: none; font-weight: 600;">
                <svg viewBox="0 0 24 24" style="width: 14px; height: 14px; fill: currentColor;"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.779-1.75-1.75s.784-1.75 1.75-1.75 1.75.779 1.75 1.75-.784 1.75-1.75 1.75zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
                LinkedIn
              </a>
            </div>
          </div>"""


    # Assemble Sidebar
    sidebar_html = f"""        <aside class="sidebar" role="complementary">
{author_card}

          <div class="sidebar-widget">
            <h4>Scheme Category</h4>
            <div class="category-badge {cat_info["class"]}">{cat_info["name"]}</div>
          </div>
          <div class="sidebar-widget">
            <h4>Related Schemes</h4>
            <ul class="related-links">
{related_links_html}            </ul>
          </div>
          <div class="sidebar-widget promo-widget">
            <h4>Need Assistance?</h4>
            <p>For official support, contact the relevant government helpdesk or visit the official portal for this scheme.</p>
          </div>
        </aside>"""

    # Official source link section at the bottom of the article
    official_source_box = f"""
            <!-- Official Source & Reference Links -->
            <div class="official-links-box" style="margin-top: 2rem; padding: 1.25rem; background: var(--bg-light); border-left: 4px solid var(--primary-color); border-radius: 4px;">
              <h3 style="margin-top: 0; font-size: 1.1rem; color: var(--primary-color);">Official Scheme References &amp; Portals</h3>
              <p style="font-size: 0.88rem; margin-bottom: 0.75rem;">Verify details, check guidelines, and apply online at the official ministries links below:</p>
              <ul style="margin: 0; padding-left: 1.25rem; font-size: 0.88rem; line-height: 1.6;">
                <li><strong>Official Scheme Website:</strong> <a href="{portal}" target="_blank" rel="noopener noreferrer">{portal.replace("https://", "").replace("http://", "")}</a></li>
                <li><strong>Central Schemes Aggregator:</strong> <a href="https://www.myscheme.gov.in" target="_blank" rel="noopener noreferrer">myscheme.gov.in</a></li>
              </ul>
            </div>"""

    # Mobile Responsiveness: Wrap table_html in responsive wrapper to prevent viewport breakages!
    if table_html:
        table_html = f'<div class="table-responsive">{table_html}</div>'

    # Assemble Full Page HTML
    page_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="{description}">
  <meta name="keywords" content="{fullname}, eligibility, benefits, how to apply, Yojana Guide">
  <meta name="robots" content="index, follow">
  <title>{fullname} - Eligibility, Benefits | Yojana Guide</title>
  <meta property="og:title" content="{fullname} - Complete Guide">
  <meta property="og:description" content="{description}">
  <meta property="og:type" content="article">
  <link rel="canonical" href="https://www.yojanaguide.in/{s["id"]}">
  <link rel="stylesheet" href="styles.css">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "{fullname} - Complete Guide",
    "description": "{description}",
    "author": {{ "@type": "Organization", "name": "Yojana Guide" }},
    "publisher": {{ "@type": "Organization", "name": "Yojana Guide" }},
    "datePublished": "2026-03-15",
    "dateModified": "2026-07-06",
    "mainEntityOfPage": "https://www.yojanaguide.in/{s["id"]}"
  }}
  </script>
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7490572944753317" crossorigin="anonymous"></script>
</head>
<body>
  <div class="reading-progress" aria-hidden="true"></div>
  <header class="site-header" role="banner">
    <div class="header-inner">
      <a href="/" class="site-logo" aria-label="Yojana Guide Home">
        <span class="logo-icon" aria-hidden="true"><svg viewBox="0 0 24 24" class="logo-svg" style="display:inline-block;vertical-align:middle;margin-right:8px;width:24px;height:24px;fill:currentColor;"><path d="M12 2L1 7v2h22V7L12 2zm9 8H3v10h3V10h3v10h2V10h2v10h3V10h2v10h3V10zm1 11H2v2h20v-2z"/></svg></span>
        <span class="logo-text">Yojana<span>Guide</span></span>
      </a>
      <nav class="main-nav" role="navigation" aria-label="Main Navigation">
        <!-- Navigation Placeholder -->
      </nav>
      <button class="hamburger" aria-label="Toggle navigation menu" aria-expanded="false"><span></span><span></span><span></span></button>
    </div>
    <div class="nav-overlay" aria-hidden="true"></div>
  </header>

  <nav class="breadcrumb" aria-label="Breadcrumb">
    <div class="container">
      <ol class="breadcrumb-list">
        <li><a href="/">Home</a></li>
        <li class="breadcrumb-separator" aria-hidden="true">›</li>
        <li><a href="categories">{cat_info["name"]}</a></li>
        <li class="breadcrumb-separator" aria-hidden="true">›</li>
        <li class="current" aria-current="page">{s["title"]}</li>
      </ol>
    </div>
  </nav>

  <main id="main-content" role="main">
    <div class="container">
      <div class="article-layout">
        <article>
          <div class="article-content">
            <div class="article-header">
              <span class="scheme-card-tag {cat_info["class"]}">{cat_info["name"]}</span>
              <h1>{fullname}</h1>
              <div class="article-meta">
                <span>Updated: July 6, 2026</span>
                <span>9 min read</span>
                <span>{cat_info["name"]}</span>
              </div>
            </div>

{toc_html}

            <h2 id="overview">Scheme Overview</h2>
            <p>{overview_text}</p>

            <h2 id="benefits">Benefits &amp; Financial Assistance</h2>
            <p>{benefits_text}</p>
{table_html}

            <h2 id="eligibility">Eligibility Criteria</h2>
{eligibility_html}
            <h3>Exclusion List</h3>
{exclusions_html}

            <h2 id="documents">Documents Required</h2>
{documents_html}

            <h2 id="apply">How to Apply</h2>
{apply_html}

            <h2 id="status">Status Check</h2>
{status_html}

            <h2 id="faq">Frequently Asked Questions (FAQs)</h2>
{faq_html}

{official_source_box}
          </div>
        </article>

{sidebar_html}
      </div>
    </div>
  </main>

  <footer class="site-footer" role="contentinfo">
    <!-- Footer Placeholder -->
  </footer>

  <button class="back-to-top" aria-label="Back to top">↑</button>
  <script src="script.js"></script>
</body>
</html>"""
    return page_html

def main():
    # 1. Compile the final list of 50 schemes
    final_schemes_list = []
    
    # Check what is in CURATED_SCHEMES first
    curated_ids = {x["id"] for x in CURATED_SCHEMES}
    
    for s_id in sorted(list(KEEP_SCHEMES)):
        if s_id in curated_ids:
            # Use curated scheme
            for cs in CURATED_SCHEMES:
                if cs["id"] == s_id:
                    final_schemes_list.append(cs)
                    break
        else:
            # Fetch from base list or build basic object
            base_s = None
            for bs in BASE_280_LIST:
                if bs["id"] == s_id:
                    base_s = bs
                    break
            
            if not base_s:
                # Fallback basic object
                base_s = {
                    "id": s_id,
                    "title": s_id.replace("-", " ").title(),
                    "desc": f"Information portal and guidelines for {s_id.replace('-', ' ').title()}.",
                    "category": "social"
                }
            
            final_schemes_list.append({
                "id": base_s["id"],
                "title": base_s["title"],
                "desc": base_s["desc"],
                "category": base_s["category"]
            })
            
    print(f"Compiled final schemes database with {len(final_schemes_list)} schemes.")
    
    # 2. Generate pages
    for s in final_schemes_list:
        html_content = generate_page(s, final_schemes_list)
        filepath = os.path.join(path, f"{s['id']}.html")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"Generated high-depth page: {s['id']}.html")

if __name__ == "__main__":
    main()
