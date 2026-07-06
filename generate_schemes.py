# -*- coding: utf-8 -*-
import os
import json

# Define Categories and their mapping
CATEGORIES = {
    "agriculture": {"name": "Agriculture & Farming", "emoji": "🌾", "class": "tag-agriculture", "color": "agriculture"},
    "health": {"name": "Health & Medical", "emoji": "🏥", "class": "tag-health", "color": "health"},
    "housing": {"name": "Housing & Shelter", "emoji": "🏠", "class": "tag-housing", "color": "housing"},
    "education": {"name": "Education & Skill Development", "emoji": "📚", "class": "tag-education", "color": "education"},
    "women": {"name": "Women & Child Development", "emoji": "👩‍👧", "class": "tag-women", "color": "women"},
    "finance": {"name": "Financial Inclusion & Business", "emoji": "💰", "class": "tag-finance", "color": "finance"},
    "employment": {"name": "Employment & Self-Employment", "emoji": "💼", "class": "tag-employment", "color": "employment"},
    "pension": {"name": "Pension & Social Security", "emoji": "👴", "class": "tag-pension", "color": "pension"}
}

# Detailed Scheme Data
SCHEMES = [
    # 1. PM Kisan
    {
        "id": "pm-kisan",
        "title": "PM Kisan Samman Nidhi",
        "fullname": "Pradhan Mantri Kisan Samman Nidhi Yojana 2026",
        "category": "agriculture",
        "emoji": "🌾",
        "description": "₹6,000 annual income support to all landholding farmer families in three equal installments of ₹2,000.",
        "meta_desc": "Complete guide to PM Kisan Samman Nidhi Yojana 2026. Check eligibility, benefits, application process, required documents, and status check steps.",
        "meta_keywords": "PM Kisan, PM Kisan Samman Nidhi, PM Kisan Eligibility, PM Kisan Status Check, PM Kisan 2026, Farmer Income Support Scheme",
        "intro": "The <strong>Pradhan Mantri Kisan Samman Nidhi (PM-KISAN)</strong> is a key central sector welfare scheme launched by the Ministry of Agriculture and Farmers' Welfare, Government of India. Introduced on February 24, 2019, the scheme aims to provide direct financial assistance to all landholding farmer families across the country to supplement their financial needs for purchasing agricultural inputs and supporting household needs.",
        "benefits_text": "Eligible families receive a financial assistance of <strong>₹6,000 per year</strong>, disbursed in three equal installments of ₹2,000 every four months. The funds are directly transferred to the Aadhaar-seeded bank accounts of the beneficiaries using the Direct Benefit Transfer (DBT) system, ensuring full transparency.",
        "table_html": """<table>
          <thead>
            <tr>
              <th>Installment</th>
              <th>Period</th>
              <th>Amount</th>
              <th>Disbursal Method</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>1st Installment</td>
              <td>April – July</td>
              <td>₹2,000</td>
              <td>Direct Benefit Transfer (DBT)</td>
            </tr>
            <tr>
              <td>2nd Installment</td>
              <td>August – November</td>
              <td>₹2,000</td>
              <td>Direct Benefit Transfer (DBT)</td>
            </tr>
            <tr>
              <td>3rd Installment</td>
              <td>December – March</td>
              <td>₹2,000</td>
              <td>Direct Benefit Transfer (DBT)</td>
            </tr>
          </tbody>
        </table>""",
        "eligibility_list": [
            "All landholding farmer families who own cultivable land in their names as per official state land records.",
            "The family unit is defined as husband, wife, and minor children.",
            "Farmers from both rural and urban areas are covered under the scheme."
        ],
        "exclusions_list": [
            "Institutional landholders.",
            "Families where one or more members hold or held constitutional posts (e.g., Ministers, MPs, MLAs).",
            "Retired or serving government employees (except Group D / Multi-Tasking Staff).",
            "Superannuated or retired pensioners with a monthly pension of ₹10,000 or more.",
            "Income tax payers in the last assessment year.",
            "Professionals like Doctors, Engineers, Lawyers, and Chartered Accountants."
        ],
        "documents_list": [
            "<strong>Aadhaar Card:</strong> Mandatory for identity and OTP verification.",
            "<strong>Land Ownership Documents:</strong> Khatauni, Jamabandi, or copy of land registration showing cultivable land ownership.",
            "<strong>Aadhaar-Linked Bank Passbook:</strong> For receiving the direct transfer.",
            "<strong>Active Mobile Number:</strong> Required for registration and SMS status updates."
        ],
        "apply_steps": [
            "Visit the official PM-Kisan portal at <strong>pmkisan.gov.in</strong>.",
            "Click on the 'New Farmer Registration' link in the Farmers Corner section.",
            "Select 'Rural Farmer Registration' or 'Urban Farmer Registration' based on your location.",
            "Enter your Aadhaar number, mobile number, select your state, and fill in the captcha, then click 'Get OTP'.",
            "Enter the OTP received on your mobile and proceed to the registration form.",
            "Fill in your personal details (District, Block, Village, Name, Category) and land ownership details (Survey/Khata Number, Dag/Khasra Number, Land Area).",
            "Upload scanned copies of land documents, enter your bank details, and click 'Submit'.",
            "Alternatively, approach your local Common Service Centre (CSC) or village Patwari/Lekhpal."
        ],
        "status_steps": [
            "Go to <strong>pmkisan.gov.in</strong>.",
            "Under 'Farmers Corner', click on 'Know Your Status'.",
            "Enter your Registration Number. If you don't know it, click 'Know your registration number' and verify using mobile or Aadhaar OTP.",
            "Enter the captcha code and click 'Get Data'. Your installment details, Aadhaar seeding status, and eligibility status will be displayed."
        ],
        "faqs": [
            {"q": "Is eKYC mandatory for PM Kisan beneficiaries?", "a": "Yes, eKYC is mandatory for all beneficiaries. You can complete it online using Aadhaar OTP on the portal or via biometrics at any CSC."},
            {"q": "What should I do if my installment is not received?", "a": "Verify if your bank account is linked with Aadhaar and Active for DBT. You should also check the 'Beneficiary Status' page on the portal for any rejection reasons like incorrect land mapping or name mismatch."},
            {"q": "Can multiple members of the same family claim benefits?", "a": "No. The scheme guidelines define a family as husband, wife, and minor children. Only one member of the family can receive the benefit on their land holding."}
        ]
    },
    # 2. Ayushman Bharat
    {
        "id": "ayushman-bharat",
        "title": "Ayushman Bharat PM-JAY",
        "fullname": "Ayushman Bharat Pradhan Mantri Jan Arogya Yojana (PM-JAY)",
        "category": "health",
        "emoji": "🏥",
        "description": "Free health insurance coverage up to ₹5 lakh per family per year for secondary and tertiary care hospitalizations.",
        "meta_desc": "Complete details of Ayushman Bharat Pradhan Mantri Jan Arogya Yojana (PM-JAY). Find eligibility, cashless hospital treatment details, and how to apply.",
        "meta_keywords": "Ayushman Bharat, PMJAY, Ayushman Card, Free Health Insurance, Government Health Scheme, Cashless Treatment",
        "intro": "<strong>Ayushman Bharat Pradhan Mantri Jan Arogya Yojana (PM-JAY)</strong> is the flagship national health insurance scheme of the Government of India, launched on September 23, 2018, by PM Narendra Modi. Touted as the world's largest government-funded healthcare program, it aims to provide free healthcare access to over 50 crore citizens representing the bottom 40% of India's population.",
        "benefits_text": "The scheme provides a health cover of <strong>₹5,00,000 (₹5 Lakh) per family per year</strong>. This coverage is completely cashless and paperless at all empanelled public and private hospitals across the country. It covers all pre-existing conditions from day one of the policy.",
        "table_html": """<table>
          <thead>
            <tr>
              <th>Feature</th>
              <th>Coverage Details</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Coverage Amount</td>
              <td>₹5 Lakh per family per year (floating basis)</td>
            </tr>
            <tr>
              <td>Pre-existing Diseases</td>
              <td>Covered from Day 1</td>
            </tr>
            <tr>
              <td>Hospitals covered</td>
              <td>All empanelled public &amp; private hospitals pan-India</td>
            </tr>
            <tr>
              <td>Pre &amp; Post Hospitalization</td>
              <td>3 days pre-hospitalization &amp; 15 days post-hospitalization costs (including medicines &amp; diagnostics)</td>
            </tr>
          </tbody>
        </table>""",
        "eligibility_list": [
            "Families identified under the Socio-Economic Caste Census (SECC) 2011 data.",
            "Rural families living in kucha houses, female-headed households, landless households, or households with disabled members.",
            "Urban families engaged in occupational categories like ragpickers, beggars, domestic workers, street vendors, construction workers, plumbers, etc.",
            "In recent updates, all senior citizens aged 70 and above, regardless of income status, are eligible to receive a separate cover of ₹5 lakh under PM-JAY."
        ],
        "exclusions_list": [
            "Families owning a motorized vehicle, fishing boat, or 3-4 wheeler agricultural equipment.",
            "Government employees.",
            "Families earning more than ₹10,000 per month.",
            "Tax-paying households.",
            "Families living in permanent (pucca) houses with modern amenities."
        ],
        "documents_list": [
            "<strong>Aadhaar Card or Ration Card:</strong> For verifying family members and identity.",
            "<strong>PM-JAY Letter / SECC Letter:</strong> Official letter sent by the government containing family ID (HHID).",
            "<strong>Active Mobile Number:</strong> For linking and mobile authentication."
        ],
        "apply_steps": [
            "Visit the official website <strong>pmjay.gov.in</strong> and click on 'Am I Eligible'.",
            "Enter your mobile number and captcha, then enter the OTP received.",
            "Search for your family using name, ration card number, mobile number, or HHID number.",
            "If your name is listed, visit the nearest empanelled hospital or Common Service Centre (CSC).",
            "Approach the 'Ayushman Mitra' desk at the hospital or the operator at the CSC.",
            "Provide your Aadhaar card and Ration Card for biometric verification.",
            "Upon successful verification, the operator will issue your customized 'Ayushman Card' (e-card) which can be used to avail cashless hospital treatments."
        ],
        "status_steps": [
            "Visit <strong>beneficiary.nha.gov.in</strong>.",
            "Log in using your mobile number and verify via OTP.",
            "Select your State, Scheme (PM-JAY), District, and Search By parameters (Aadhaar/Ration Card/Name).",
            "View the verification status of all family members. You can download active Ayushman cards directly from this portal."
        ],
        "faqs": [
            {"q": "Is there a limit on family size under PM-JAY?", "a": "No, there is no restriction on family size, age, or gender under PM-JAY. All members listed in the official ration card or SECC data can avail the benefits."},
            {"q": "Do I need to pay any premium for the Ayushman Card?", "a": "No, the scheme is completely free. No premium or card charge is levied on eligible beneficiaries at government desks."},
            {"q": "Can I get treatment in another state?", "a": "Yes. PM-JAY offers national portability, meaning a beneficiary can get free treatment at any empanelled hospital across any state in India."}
        ]
    },
    # 3. PM Ujjwala Yojana
    {
        "id": "ujjwala-yojana",
        "title": "PM Ujjwala Yojana",
        "fullname": "Pradhan Mantri Ujjwala Yojana (PMUY) 2.0",
        "category": "women",
        "emoji": "🔥",
        "description": "Free LPG connection with first cylinder and stove to adult women from poor households.",
        "meta_desc": "Learn about PM Ujjwala Yojana (PMUY) 2.0. Check eligibility, benefits, application steps, and document checklist for free LPG gas connections.",
        "meta_keywords": "PM Ujjwala Yojana, PMUY, Free LPG Connection, Gas Cylinder Subsidy, Women Welfare Scheme",
        "intro": "The <strong>Pradhan Mantri Ujjwala Yojana (PMUY)</strong> was launched by Prime Minister Narendra Modi on May 1, 2016, with the aim of providing clean cooking fuel like LPG to women from Below Poverty Line (BPL) households. PMUY 2.0 was launched in August 2021 to provide additional free connections with simplified paperwork, particularly helping migrant families who may not have traditional address proofs.",
        "benefits_text": "PM Ujjwala Yojana provides a free LPG connection with a deposit-free 14.2 kg or 5 kg cylinder. Under PMUY 2.0, the government also provides the first LPG refill and a hotplate (gas stove) completely free of charge. Beneficiaries also receive a targeted subsidy of ₹300 per cylinder for up to 12 refills a year.",
        "table_html": """<table>
          <thead>
            <tr>
              <th>Benefit Item</th>
              <th>Cost to Beneficiary</th>
              <th>Government Contribution</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>LPG Connection Deposit</td>
              <td>₹0 (Free)</td>
              <td>Covered by Government (₹1,600 value)</td>
            </tr>
            <tr>
              <td>First LPG Refill (14.2 kg)</td>
              <td>₹0 (Free)</td>
              <td>Provided Free</td>
            </tr>
            <tr>
              <td>Single Burner Gas Stove</td>
              <td>₹0 (Free)</td>
              <td>Provided Free</td>
            </tr>
            <tr>
              <td>Cylinder Subsidy</td>
              <td>Targeted Refill Cost</td>
              <td>₹300 subsidy per cylinder (up to 12 refills/year)</td>
            </tr>
          </tbody>
        </table>""",
        "eligibility_list": [
            "The applicant must be an adult woman (aged 18 or above).",
            "The applicant must belong to a poor household (BPL/SECC list or low-income category).",
            "There must not be any existing LPG connection in the same household.",
            "The applicant must belong to one of the specified categories: SC/ST, PMAY households, Antyodaya Anna Yojana (AAY), forest dwellers, most backward classes, tea/ex-tea garden tribes, or residing in river islands."
        ],
        "exclusions_list": [
            "Households already possessing an active LPG connection from any gas agency (Indane, HP, Bharat Gas).",
            "Male applicants (only adult women can apply)."
        ],
        "documents_list": [
            "<strong>Aadhaar Card:</strong> For the applicant and all adult family members.",
            "<strong>Ration Card:</strong> Issued by the State Government, proving family composition.",
            "<strong>Bank Account Number & IFSC:</strong> For receiving LPG subsidy transfers.",
            "<strong>Proof of Address:</strong> (If different from Aadhaar, though simplified for migrant workers under self-declaration)."
        ],
        "apply_steps": [
            "Visit the official PMUY portal at <strong>pmuy.gov.in</strong>.",
            "Click on 'Apply for New Ujjwala 2.0 Connection'.",
            "Select your preferred distributor (IndianOil, Bharat Petroleum, or Hindustan Petroleum) to open their portal.",
            "Fill in the online application form with the applicant's Aadhaar, family details, bank account, and contact information.",
            "Upload the scanned copy of your Aadhaar card and Ration Card.",
            "Submit the form. Upon approval, the selected gas agency distributor will contact you.",
            "Alternatively, visit the nearest LPG distributor office, collect the physical application form, fill it, and attach photocopies of required documents."
        ],
        "status_steps": [
            "Visit the portal of the selected gas agency distributor (e.g., mylpg.in or px.indane.co.in).",
            "Log in using your reference number and registration ID.",
            "Check the status of your connection application. Once approved, visit the distributor to collect the gas cylinder and stove."
        ],
        "faqs": [
            {"q": "Can a migrant apply for Ujjwala 2.0 without a local address proof?", "a": "Yes. Under PMUY 2.0, migrants can submit a self-declaration of address as proof of residence, eliminating the need for a local domicile certificate."},
            {"q": "Is the gas stove really free?", "a": "Yes, under the updated Ujjwala 2.0 guidelines, the first stove (hotplate) and the first filled cylinder are provided entirely free of cost by the government."},
            {"q": "How is the subsidy amount paid?", "a": "The subsidy of ₹300 per cylinder is credited directly to the beneficiary's Aadhaar-linked bank account within a few days of purchasing a refill."}
        ]
    },
    # 4. PM Awas Yojana
    {
        "id": "pm-awas",
        "title": "PM Awas Yojana",
        "fullname": "Pradhan Mantri Awas Yojana (PMAY) 2.0",
        "category": "housing",
        "emoji": "🏠",
        "description": "Financial assistance and interest subsidies for building or purchasing affordable pucca houses.",
        "meta_desc": "Comprehensive guide to Pradhan Mantri Awas Yojana (PMAY) Urban and Rural. Check eligibility, housing subsidies, and online application process.",
        "meta_keywords": "PM Awas Yojana, PMAY, Affordable Housing Scheme, Credit Linked Subsidy, Home Loan Subsidy",
        "intro": "<strong>Pradhan Mantri Awas Yojana (PMAY)</strong> is a flagship housing mission launched by the Government of India on June 25, 2015. It has two components: PMAY-Urban (PMAY-U) and PMAY-Gramin (PMAY-G) for rural areas. In 2024, the government approved PMAY 2.0 to build an additional 3 crore affordable houses across urban and rural India to fulfill the vision of 'Housing for All'.",
        "benefits_text": "PMAY provides financial assistance to construct houses. In rural areas, it offers a direct grant of ₹1.2 lakh (plains) to ₹1.3 lakh (hilly/difficult areas) along with MGNREGA labor support. In urban areas, it offers interest subsidies up to 6.5% on home loans under the Credit Linked Subsidy Scheme (CLSS) for different income brackets.",
        "table_html": """<table>
          <thead>
            <tr>
              <th>Category</th>
              <th>Annual Income Bracket</th>
              <th>Max Loan Amount for Subsidy</th>
              <th>Interest Subsidy Rate</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>EWS (Economically Weaker)</td>
              <td>Up to ₹3 Lakh</td>
              <td>₹6 Lakh</td>
              <td>6.5%</td>
            </tr>
            <tr>
              <td>LIG (Low Income Group)</td>
              <td>₹3 Lakh – ₹6 Lakh</td>
              <td>₹6 Lakh</td>
              <td>6.5%</td>
            </tr>
            <tr>
              <td>MIG-I (Middle Income I)</td>
              <td>₹6 Lakh – ₹12 Lakh</td>
              <td>₹9 Lakh</td>
              <td>4.0%</td>
            </tr>
            <tr>
              <td>MIG-II (Middle Income II)</td>
              <td>₹12 Lakh – ₹18 Lakh</td>
              <td>₹12 Lakh</td>
              <td>3.0%</td>
            </tr>
          </tbody>
        </table>""",
        "eligibility_list": [
            "The beneficiary family must not own a pucca house anywhere in India in the name of any family member.",
            "The beneficiary family must fall within the defined income brackets (EWS, LIG, MIG).",
            "For urban housing, a female member of the household must be a co-owner of the property (mandatory for EWS/LIG categories)."
        ],
        "exclusions_list": [
            "Any family owning a brick-and-mortar permanent (pucca) house in India.",
            "High-income families earning above ₹18 lakh annually (unless applying under special state schemes)."
        ],
        "documents_list": [
            "<strong>Aadhaar Card:</strong> Of all family members.",
            "<strong>Income Proof:</strong> Salary slip, Form 16, or income certificate issued by local revenue authority.",
            "<strong>Land/Property Documents:</strong> Certificate of non-owning or land registration papers for self-construction.",
            "<strong>Bank Account Details:</strong> Passbook copy for direct subsidy transfer."
        ],
        "apply_steps": [
            "For Urban: Visit the official PMAY portal at <strong>pmaymis.gov.in</strong>.",
            "Click on 'Citizen Assessment' and select 'Apply Online'.",
            "Select your application category (e.g., Slum Redevelopment, Benefit under Charge, or CLSS).",
            "Enter your Aadhaar number and click 'Check' to verify.",
            "Fill in the detailed form including family income, bank account details, and current address.",
            "Submit the application and download the assessment ID printout.",
            "For Rural: The beneficiary lists are generated by state governments using SECC 2011 and Awaas+ surveys. Visit your local Gram Panchayat office to check inclusion or submit your registration request."
        ],
        "status_steps": [
            "Visit <strong>pmaymis.gov.in</strong>.",
            "Click on 'Citizen Assessment' and select 'Track Your Assessment Status'.",
            "Select track by 'Name, Father's Name & Mobile No' or 'Assessment ID'.",
            "Enter details and click 'Submit' to check application progress."
        ],
        "faqs": [
            {"q": "What is the maximum subsidy amount under PMAY?", "a": "The maximum subsidy amount under the CLSS component is approximately ₹2.67 lakh, which is credited directly to the beneficiary's home loan account, reducing the outstanding principal."},
            {"q": "Who is included in a 'family' under PMAY?", "a": "A beneficiary family includes husband, wife, and unmarried children. An adult earning member can be treated as a separate household if they do not own a house."},
            {"q": "Can I apply for PMAY online if I want to build a house in a village?", "a": "For villages (PMAY-G), you cannot apply directly online. The list is finalized by Gram Sabhas based on SECC 2011 data. You should contact your local Panchayat representative or Gram Sevak."}
        ]
    },
    # 5. Sukanya Samriddhi Yojana
    {
        "id": "sukanya-samriddhi",
        "title": "Sukanya Samriddhi Yojana",
        "fullname": "Sukanya Samriddhi Account Yojana (SSY)",
        "category": "women",
        "emoji": "👧",
        "description": "High-interest savings scheme for the girl child under 'Beti Bachao Beti Padhao' with triple tax benefits.",
        "meta_desc": "Complete guide to Sukanya Samriddhi Yojana (SSY) 2026. Learn about interest rates, eligibility, tax benefits, and how to open an account.",
        "meta_keywords": "Sukanya Samriddhi Yojana, SSY Account, Girl Child Savings Scheme, Post Office SSY, SSY Interest Rate 2026",
        "intro": "<strong>Sukanya Samriddhi Yojana (SSY)</strong> is a small deposit scheme for the girl child, launched on January 22, 2015, by Prime Minister Narendra Modi as part of the 'Beti Bachao Beti Padhao' campaign. The scheme is designed to encourage families to save for the higher education and marriage expenses of their female children, offering one of the highest interest rates among government savings schemes.",
        "benefits_text": "The scheme offers a highly competitive interest rate (currently <strong>8.2% for 2026</strong>), compounded annually. Deposits qualify for tax deductions under Section 80C, the interest earned is tax-free, and the final maturity amount is also completely exempt from income tax (EEE status).",
        "table_html": """<table>
          <thead>
            <tr>
              <th>Feature</th>
              <th>Details</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Current Interest Rate (2026)</td>
              <td>8.2% (Compounded Annually)</td>
            </tr>
            <tr>
              <td>Min/Max Deposit per Year</td>
              <td>₹250 / ₹1.5 Lakh</td>
            </tr>
            <tr>
              <td>Deposit Period</td>
              <td>15 years from account opening</td>
            </tr>
            <tr>
              <td>Account Maturity</td>
              <td>21 years from account opening (or marriage after age 18)</td>
            </tr>
            <tr>
              <td>Tax Status</td>
              <td>Exempt-Exempt-Exempt (EEE) under Section 80C</td>
            </tr>
          </tbody>
        </table>""",
        "eligibility_list": [
            "The account can be opened only by the natural or legal guardian of a girl child.",
            "The girl child must be a resident Indian citizen.",
            "The girl child must be under the age of 10 years at the time of account opening.",
            "Only one account can be opened for a single girl child, with a maximum of two accounts per family (three in case of twins/triplets)."
        ],
        "exclusions_list": [
            "Non-resident Indians (NRIs) and Overseas Citizens of India (OCIs) cannot open or maintain an SSY account.",
            "Male children cannot be beneficiaries of this scheme."
        ],
        "documents_list": [
            "<strong>Girl Child Birth Certificate:</strong> Mandatory to prove age and relation.",
            "<strong>Guardian's ID Proof:</strong> Aadhaar Card, PAN Card, Voter ID, or Passport.",
            "<strong>Guardian's Address Proof:</strong> Electricity bill, Aadhaar, or ration card.",
            "<strong>Photographs:</strong> Passport-size photos of the guardian and the girl child."
        ],
        "apply_steps": [
            "Visit any authorized commercial bank branch or your nearest Post Office.",
            "Ask for the 'Sukanya Samriddhi Account Opening Form'.",
            "Fill in the details of the girl child (Name, Date of Birth) and the guardian.",
            "Attach the required documents (Birth certificate, Guardian PAN/Aadhaar, Photos).",
            "Submit the form and make the initial deposit (minimum ₹250).",
            "The Post Office/Bank will issue an account passbook containing details like the girl's name, DOB, account number, and date of opening."
        ],
        "status_steps": [
            "To check status or balance, register for Internet Banking or Mobile Banking with the respective bank or Post Office.",
            "Log in to the portal and view the linked SSY account details.",
            "The physical passbook can also be updated regularly by visiting the branch."
        ],
        "faqs": [
            {"q": "What happens if I fail to deposit the minimum amount?", "a": "If the minimum deposit of ₹250 per year is not paid, the account will be defaulted. It can be regularized by paying a penalty of ₹50 per year along with the minimum deposit amount for the missed years."},
            {"q": "Can I withdraw money before maturity?", "a": "Partial withdrawal up to 50% of the account balance at the end of the preceding financial year is allowed for the girl child's higher education, after she attains the age of 18 or passes Class 10."},
            {"q": "Does the account close automatically after 21 years?", "a": "Yes, the account matures 21 years after the date of opening. If the girl child gets married after turning 18, the account can be closed early by submitting a marriage declaration."}
        ]
    },
    # 6. PM Mudra Yojana
    {
        "id": "mudra-yojana",
        "title": "PM Mudra Yojana",
        "fullname": "Pradhan Mantri MUDRA Yojana (PMMY)",
        "category": "finance",
        "emoji": "💼",
        "description": "Collateral-free business loans up to ₹10 lakh for non-corporate, non-farm small/micro enterprises.",
        "meta_desc": "Check eligibility, loan limits, Shishu, Kishore, and Tarun categories, and how to apply for collateral-free business loans under PM Mudra Yojana.",
        "meta_keywords": "PM Mudra Yojana, Mudra Loan, Business Loan Scheme, Shishu Kishore Tarun, Collateral Free Loan",
        "intro": "<strong>Pradhan Mantri MUDRA Yojana (PMMY)</strong> is a flagship financial inclusion scheme launched on April 8, 2015, by Prime Minister Narendra Modi. The scheme is designed to provide loans up to ₹10 lakh (increased to ₹20 lakh in recent budget expansions) to small business owners, shopkeepers, artisans, and startup entrepreneurs who run non-corporate, non-farm small and micro enterprises.",
        "benefits_text": "MUDRA (Micro Units Development & Refinance Agency) acts as a refinancing institution. The key benefit of a Mudra loan is that it is <strong>collateral-free</strong> (no security required) and has competitive interest rates with flexible repayment terms of up to 5 years. Loans are categorized into three stages based on funding requirements.",
        "table_html": """<table>
          <thead>
            <tr>
              <th>Loan Category</th>
              <th>Target Funding Limit</th>
              <th>Suitable For</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Shishu</td>
              <td>Up to ₹50,000</td>
              <td>New startups, micro-vendors, small shops</td>
            </tr>
            <tr>
              <td>Kishore</td>
              <td>₹50,000 to ₹5 Lakh</td>
              <td>Established businesses looking to buy equipment or inventory</td>
            </tr>
            <tr>
              <td>Tarun</td>
              <td>₹5 Lakh to ₹10 Lakh</td>
              <td>Expanding businesses requiring larger capital (Budget 2024 increased limit up to ₹20 Lakh under special conditions)</td>
            </tr>
          </tbody>
        </table>""",
        "eligibility_list": [
            "Any Indian citizen who has a viable business plan for a non-farm income-generating activity.",
            "Activities include manufacturing, processing, trading, or service sector industries.",
            "Micro and small enterprises, proprietorships, partnerships, and small-scale manufacturing units are eligible."
        ],
        "exclusions_list": [
            "Corporate bodies/large industries.",
            "Farming/agricultural activities (though allied activities like poultry, dairy, and beekeeping are eligible)."
        ],
        "documents_list": [
            "<strong>Mudra Application Form:</strong> Specific to Shishu, Kishore, or Tarun categories.",
            "<strong>Identity & Address Proof:</strong> Aadhaar Card, Voter ID, PAN Card, Driving License.",
            "<strong>Business Proof:</strong> Registration certificate, license, tax registration, or shop establishment certificate.",
            "<strong>Financial Statements:</strong> (For Kishore & Tarun) Last 2 years balance sheet, IT returns, and bank statements."
        ],
        "apply_steps": [
            "Prepare a viable business plan outlining your activity, expenses, and projected profits.",
            "Approach any commercial bank, regional rural bank, co-operative bank, or micro-finance institution.",
            "Submit the completed Mudra application form along with the required documents.",
            "The bank will verify your creditworthiness, business viability, and process the loan.",
            "Alternatively, apply online through the <strong>Udyam Mitra</strong> portal (udyamimitra.in) or bank-specific portals.",
            "Once approved, you will receive a <strong>Mudra RuPay Card</strong>, which works like a credit/debit card to withdraw working capital."
        ],
        "status_steps": [
            "Track your application status via the Udyam Mitra portal using your reference number.",
            "Contact your respective bank branch where you submitted the physical documents for regular tracking updates."
        ],
        "faqs": [
            {"q": "What is a Mudra Card?", "a": "A Mudra Card is a debit card issued against the Mudra loan account for working capital requirements. It allows the entrepreneur to make transactions and withdraw cash in a flexible manner, paying interest only on the utilized amount."},
            {"q": "Is a guarantor required for a Mudra Loan?", "a": "No. Under the Credit Guarantee Fund for Micro Units (CGFMU), no third-party guarantee or collateral is required for Mudra loans."},
            {"q": "What is the interest rate for Mudra Loans?", "a": "Interest rates vary from bank to bank and are linked to the RBI's Marginal Cost of Funds Based Lending Rate (MCLR). Typically, it ranges between 8.5% and 12% per annum."}
        ]
    },
    # 7. PM Surya Ghar
    {
        "id": "pm-surya-ghar",
        "title": "PM Surya Ghar: Muft Bijli Yojana",
        "fullname": "PM Surya Ghar Muft Bijli Yojana 2026",
        "category": "housing",
        "emoji": "☀️",
        "description": "Subsidy scheme to install rooftop solar panels, providing up to 300 units of free electricity per month for 1 crore households.",
        "meta_desc": "Complete information on PM Surya Ghar Muft Bijli Yojana. Learn about rooftop solar panel subsidies, eligibility, and online application steps.",
        "meta_keywords": "PM Surya Ghar, Muft Bijli Yojana, Rooftop Solar Subsidy, Free Electricity Scheme, Solar Panel Yojana",
        "intro": "The <strong>PM Surya Ghar: Muft Bijli Yojana</strong> is a progressive rooftop solar subsidy initiative launched by the Government of India in February 2024 with a total outlay of ₹75,000 crore. The scheme aims to light up 1 crore households across India by providing them up to 300 units of free electricity monthly through rooftop solar installations, while generating income through selling surplus power back to the grid.",
        "benefits_text": "The government provides substantial direct subsidies for solar installations up to 3 kW capacity. In addition, households get free electricity up to 300 units every month, saving thousands on electricity bills annually. Low-interest collateral-free loans are also facilitated for the remaining installation cost.",
        "table_html": """<table>
          <thead>
            <tr>
              <th>Rooftop Solar Capacity</th>
              <th>Estimated Cost</th>
              <th>Government Subsidy</th>
              <th>Bank Loan Facility</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>1 kW</td>
              <td>₹50,000 – ₹55,000</td>
              <td>₹30,000</td>
              <td>~₹20,000</td>
            </tr>
            <tr>
              <td>2 kW</td>
              <td>₹1,00,000 – ₹1,10,000</td>
              <td>₹60,000</td>
              <td>~₹40,000</td>
            </tr>
            <tr>
              <td>3 kW or Above</td>
              <td>₹1,45,000 – ₹1,55,000</td>
              <td>₹78,000 (Max Subsidy)</td>
              <td>Remaining amount</td>
            </tr>
          </tbody>
        </table>""",
        "eligibility_list": [
            "The applicant must be an Indian citizen.",
            "The household must have a suitable roof (concrete or sheet) with sufficient sunlight access.",
            "The applicant must have an active consumer number with a local electricity distribution company (DISCOM).",
            "The applicant must not have availed of any other solar rooftop subsidy previously."
        ],
        "exclusions_list": [
            "Commercial or industrial buildings (the scheme is strictly for residential households).",
            "Buildings without an official electricity connection."
        ],
        "documents_list": [
            "<strong>Aadhaar Card:</strong> Proof of identity.",
            "<strong>Electricity Bill:</strong> Recent bill showing consumer number and average usage.",
            "<strong>Bank Account Passbook:</strong> For receiving the subsidy credit.",
            "<strong>Roof Ownership Proof:</strong> Or NOC if renting/in apartment."
        ],
        "apply_steps": [
            "Register on the national portal at <strong>pmsuryaghar.gov.in</strong>.",
            "Select your State and Electricity Distribution Company (DISCOM), and enter your consumer account number.",
            "Enter your mobile number and email to verify registration via OTP.",
            "Log in using your consumer number and mobile, and apply for rooftop solar.",
            "Submit roof details, bank account, and upload a copy of your electricity bill.",
            "Wait for feasibility approval from your DISCOM.",
            "Once approved, get the solar plant installed by any of the registered vendors in your DISCOM.",
            "After installation, submit the net metering application and upload photos of the plant on the portal.",
            "A DISCOM inspector will inspect the site, install the net meter, and issue a commissioning certificate.",
            "Upon commissioning, submit your bank details on the portal. The subsidy will be credited directly to your bank account within 30 days."
        ],
        "status_steps": [
            "Log in to the national portal <strong>pmsuryaghar.gov.in</strong>.",
            "Click on 'Track Application Status' to view feasibility, installation, commissioning, and subsidy release status."
        ],
        "faqs": [
            {"q": "What is the lifespan of solar panels under this scheme?", "a": "Solar panels generally come with a performance warranty of 25 years, making it a highly profitable long-term investment."},
            {"q": "Can I apply for a loan to install the solar plant?", "a": "Yes, nationalized banks offer collateral-free loans at attractive interest rates (approx. 7% per annum) for installing rooftop solar up to 3 kW capacity."},
            {"q": "How does net metering work?", "a": "A net meter records both the electricity you consume from the grid and the excess solar electricity you export to the grid. Your bill is generated based on the net difference."}
        ]
    },
    # 8. Lakhpati Didi Scheme
    {
        "id": "lakhpati-didi",
        "title": "Lakhpati Didi Scheme",
        "fullname": "Lakhpati Didi Yojana 2026",
        "category": "women",
        "emoji": "👩‍👧",
        "description": "Skill training, financial literacy, and loan support program to help Self-Help Group (SHG) women earn over ₹1 lakh annually.",
        "meta_desc": "Discover the Lakhpati Didi Scheme details. Check training programs, financial support, eligibility, and how women Self-Help Group members can apply.",
        "meta_keywords": "Lakhpati Didi Scheme, Lakhpati Didi Yojana, SHG Women Scheme, Skill India Women, Women Livelihood Scheme",
        "intro": "The <strong>Lakhpati Didi Scheme</strong> is an ambitious national program launched by the Ministry of Rural Development, Government of India. The primary objective is to empower women members of Self-Help Groups (SHGs) by providing them with skill development training, financial literacy, and business tools to enable them to earn a sustainable income of at least <strong>₹1,00,000 (₹1 Lakh) per year</strong>. In the 2024 budget, the target was expanded to cover 3 crore SHG women across India.",
        "benefits_text": "Women under this scheme receive free vocational training in modern sectors like LED bulb manufacturing, drone operation, tailoring, plumbing, and agriculture. They also get access to interest-free or low-interest microloans, financial literacy workshops, and direct market linkage through government e-commerce platforms (like GeM).",
        "table_html": """<table>
          <thead>
            <tr>
              <th>Program Component</th>
              <th>Support Provided</th>
              <th>Objective</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Skill Training</td>
              <td>Free technical &amp; vocational courses</td>
              <td>Enable independent entrepreneurship</td>
            </tr>
            <tr>
              <td>Drone Didi Initiative</td>
              <td>Training in agricultural drone operations</td>
              <td>Provide drone rental services to farmers</td>
            </tr>
            <tr>
              <td>Financial Assistance</td>
              <td>Collateral-free micro-loans through SHGs</td>
              <td>Business capital requirements</td>
            </tr>
            <tr>
              <td>Market Linkage</td>
              <td>Access to e-commerce, local melas, and GeM portal</td>
              <td>Sell products directly to buyers/government</td>
            </tr>
          </tbody>
        </table>""",
        "eligibility_list": [
            "The applicant must be a resident woman of India.",
            "The applicant must be an active member of a registered Self-Help Group (SHG) in her village/town.",
            "The family annual income must be low, with a focus on economically weaker sections."
        ],
        "exclusions_list": [
            "Women who are not part of any Self-Help Group (they must first join/form an SHG).",
            "Families with permanent government employment."
        ],
        "documents_list": [
            "<strong>Aadhaar Card:</strong> Proof of identity.",
            "<strong>SHG Membership Certificate/ID Card:</strong> Proving active membership.",
            "<strong>Income Certificate:</strong> Proving low-income bracket.",
            "<strong>Bank Account Details:</strong> Bank passbook of both the individual and the SHG."
        ],
        "apply_steps": [
            "Join or form a Self-Help Group (SHG) in your local village or urban ward.",
            "Contact your local Anganwadi center, Gram Panchayat, or Block Development Office (BDO).",
            "Express interest in the 'Lakhpati Didi' training program during SHG weekly/monthly meetings.",
            "The Block Nodal Officer under the National Rural Livelihoods Mission (NRLM) will verify active SHGs and enroll eligible candidates.",
            "Choose your desired training sector (e.g., Drone pilot, LED repair, tailoring, mushroom farming).",
            "Upon completion of the training, you can submit a business proposal through your SHG to secure microfinance/loans from linked banks."
        ],
        "status_steps": [
            "Enrolled SHG members can check their status through the NRLM state portals or by inquiring with the block-level Livelihood Nodal Officer."
        ],
        "faqs": [
            {"q": "What is the 'Namo Drone Didi' scheme?", "a": "It is a sub-component of the Lakhpati Didi initiative where select SHG women are trained to fly and maintain drones for agricultural spraying and crop monitoring, earning high rental income from farmers."},
            {"q": "Is there any direct cash transfer under Lakhpati Didi?", "a": "No, this is a capacity-building and livelihood support scheme. Benefits are provided in the form of free training, toolkits, and access to bank credits rather than direct cash hand-outs."},
            {"q": "What is the interest rate on loans under this scheme?", "a": "Loans are provided through SHG-bank linkages, which often carry highly subsidized interest rates, and in many states, interest-subvention makes them virtually interest-free."}
        ]
    },
    # 9. PM Vishwakarma
    {
        "id": "pm-vishwakarma",
        "title": "PM Vishwakarma Yojana",
        "fullname": "PM Vishwakarma Scheme 2026",
        "category": "education",
        "emoji": "🛠️",
        "description": "End-to-end support for traditional artisans and craftspeople, including skill training, toolkit incentives, and collateral-free loans.",
        "meta_desc": "Understand the PM Vishwakarma Yojana. Details on training allowance, ₹15,000 toolkit incentive, interest-subvented business loans, and online application.",
        "meta_keywords": "PM Vishwakarma Yojana, Artisan Support Scheme, Toolkit Incentive Scheme, Vishwakarma Loan, Skill India",
        "intro": "The <strong>PM Vishwakarma Yojana</strong> was launched by Prime Minister Narendra Modi on September 17, 2023, with a budget of ₹13,000 crore. The scheme is dedicated to providing holistic support to traditional artisans and craftspeople (Vishwakarmas) working with their hands and tools. It covers 18 traditional trades including carpenters, blacksmiths, potters, weavers, cobblers, and sculptors.",
        "benefits_text": "Artisans receive a formal Vishwakarma Certificate and ID, basic and advanced skill training with a stipend of ₹500/day, a toolkit incentive of ₹15,000, and access to collateral-free enterprise loans up to ₹3 lakh in two tranches at a highly subsidized interest rate of 5%.",
        "table_html": """<table>
          <thead>
            <tr>
              <th>Benefit Type</th>
              <th>Details &amp; Amount</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Training Stipend</td>
              <td>₹500 per day during basic (5-7 days) &amp; advanced (15+ days) training</td>
            </tr>
            <tr>
              <td>Toolkit Incentive</td>
              <td>₹15,000 e-voucher or cash transfer to purchase modern tools</td>
            </tr>
            <tr>
              <td>Subsidized Loan</td>
              <td>Up to ₹3 Lakh (Tranche 1: ₹1 Lakh, Tranche 2: ₹2 Lakh) at 5% interest rate</td>
            </tr>
            <tr>
              <td>Digital Transaction Incentive</td>
              <td>₹1 cashback per digital transaction (up to 100 transactions/month)</td>
            </tr>
          </tbody>
        </table>""",
        "eligibility_list": [
            "An artisan or craftsperson working in one of the 18 family-based traditional trades (e.g. Carpenter, Boat Maker, Blacksmith, Hammer Maker, Locksmith, Sculptor, Goldsmith, Potter, Cobbler, Mason, Basket Maker, Toy Maker, Barber, Garland Maker, Washerman, Tailor, Fishing Net Maker).",
            "The applicant must be at least 18 years old.",
            "Only one member of a family (husband, wife, unmarried children) can apply under the scheme."
        ],
        "exclusions_list": [
            "Government employees and their family members.",
            "Individuals who have already availed of loans under similar self-employment schemes (PMEGP, Mudra, PM SVANidhi) in the last 3 years."
        ],
        "documents_list": [
            "<strong>Aadhaar Card:</strong> For identity verification.",
            "<strong>Mobile Number:</strong> Aadhaar-linked for OTP generation.",
            "<strong>Bank Account Passbook:</strong> For receiving stipend and toolkit incentives.",
            "<strong>Ration Card:</strong> Mandatory to establish family definition."
        ],
        "apply_steps": [
            "Visit your nearest Common Service Centre (CSC) as self-registration is not allowed without biometrics.",
            "Carry your Aadhaar, bank passbook, and mobile phone.",
            "The CSC operator will register you on the PM Vishwakarma portal (pmvishwakarma.gov.in) using Aadhaar biometric authentication.",
            "Select your trade/craft and enter your family details.",
            "Submit the registration. The application will undergo a 3-tier verification: Gram Panchayat/ULB level, District Committee level, and Screening Committee level.",
            "Once approved, you will be scheduled for a 5-day basic training program. You will receive your Vishwakarma Digital Certificate and ID."
        ],
        "status_steps": [
            "Artisans can track their application verification status on the official portal <strong>pmvishwakarma.gov.in</strong> by logging in with their registered mobile number."
        ],
        "faqs": [
            {"q": "What is the repayment period for Vishwakarma Loans?", "a": "For the first tranche loan of ₹1 lakh, the repayment tenure is 18 months. For the second tranche of ₹2 lakh, the repayment period is 30 months."},
            {"q": "Do I need to submit collateral for the loan?", "a": "No, the loan is collateral-free. The Government of India acts as the guarantor for the credit."},
            {"q": "Is the skill training training program free?", "a": "Yes, the training is free, and the government pays the participant a stipend of ₹500 per day to compensate for wage loss."}
        ]
    },
    # 10. PM Jan Dhan Yojana
    {
        "id": "jan-dhan",
        "title": "PM Jan Dhan Yojana",
        "fullname": "Pradhan Mantri Jan-Dhan Yojana (PMJDY)",
        "category": "finance",
        "emoji": "💰",
        "description": "National financial inclusion scheme offering zero-balance bank accounts with free Rupay debit card, insurance, and overdraft facility.",
        "meta_desc": "Complete guide on PM Jan Dhan Yojana (PMJDY) account opening. Details on zero-balance account features, ₹10,000 overdraft, and Rupay insurance.",
        "meta_keywords": "PM Jan Dhan Yojana, PMJDY Account, Zero Balance Account, Rupay Debit Card, Overdraft Facility",
        "intro": "<strong>Pradhan Mantri Jan-Dhan Yojana (PMJDY)</strong> is India's national mission for financial inclusion, launched on August 28, 2014, by PM Narendra Modi. The scheme was introduced to ensure that every household in India has access to a bank account, providing basic financial services like savings, deposits, remittances, insurance, and pension facilities to the unbanked population.",
        "benefits_text": "PMJDY accounts are <strong>zero-balance accounts</strong> (no minimum balance required). Account-holders receive a free <strong>RuPay Debit Card</strong> with built-in accident insurance cover of ₹2 lakh. After 6 months of satisfactory account operation, an overdraft facility of up to <strong>₹10,000</strong> is made available, particularly targeting the lady of the household.",
        "table_html": """<table>
          <thead>
            <tr>
              <th>Feature</th>
              <th>Benefit Details</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Minimum Balance</td>
              <td>₹0 (No minimum balance charges)</td>
            </tr>
            <tr>
              <td>Accident Insurance Cover</td>
              <td>₹2 Lakh (with RuPay Card)</td>
            </tr>
            <tr>
              <td>Overdraft Facility</td>
              <td>Up to ₹10,000 (No security required)</td>
            </tr>
          </tbody>
        </table>""",
        "eligibility_list": [
            "Any resident Indian citizen aged 10 years or above.",
            "Particularly designed for individuals who do not possess any other bank account."
        ],
        "exclusions_list": [
            "Individuals who already own regular active savings bank accounts."
        ],
        "documents_list": [
            "<strong>Aadhaar Card:</strong> Serves as both identity and address proof.",
            "<strong>If Aadhaar is not available:</strong> Officially Valid Documents (OVD) like Voter ID, PAN Card, Driving License, or NREGA Job Card."
        ],
        "apply_steps": [
            "Visit any commercial bank branch, regional rural bank, or authorized Bank Mitra (Business Correspondent).",
            "Ask for the 'PM Jan Dhan Account Opening Form'.",
            "Fill in your personal details (Name, Address, Occupation, Mobile) and check the box for 'Zero Balance Account'.",
            "Attach a copy of your Aadhaar card and passport-size photographs.",
            "Submit the form. The bank will open the account and issue your Passbook and RuPay Debit Card."
        ],
        "status_steps": [
            "Track account activation by checking with the bank branch or verifying via mobile SMS notification when the account is opened."
        ],
        "faqs": [
            {"q": "What is the overdraft age limit?", "a": "The age limit for availing the overdraft facility of ₹10,000 is 18 to 65 years."},
            {"q": "Can I transfer funds from my Jan Dhan account?", "a": "Yes, Jan Dhan accounts support all regular banking services including mobile banking, net banking, and direct fund transfers."},
            {"q": "Is there any check required to keep the accident insurance active?", "a": "Yes, the RuPay Card must be used for at least one successful financial or non-financial transaction at an ATM, POS, or online channel within 90 days prior to the accident."}
        ]
    },
    # 11. Atal Pension Yojana
    {
        "id": "atal-pension",
        "title": "Atal Pension Yojana",
        "fullname": "Atal Pension Yojana (APY)",
        "category": "pension",
        "emoji": "👴",
        "description": "Co-contribution pension scheme for unorganized sector workers offering guaranteed minimum pension of ₹1,000 to ₹5,000 per month after age 60.",
        "meta_desc": "Learn about the Atal Pension Yojana (APY). Monthly premium tables, eligibility criteria, guaranteed pension levels, and how to enroll.",
        "meta_keywords": "Atal Pension Yojana, APY Pension, Pension Scheme Unorganized Sector, APY Calculator, APY Enrollment",
        "intro": "<strong>Atal Pension Yojana (APY)</strong> was launched by PM Narendra Modi on May 9, 2015, targeting workers in the unorganized sector (like delivery agents, maids, gardeners, drivers, and agricultural laborers). Administered by the Pension Fund Regulatory and Development Authority (PFRDA), the scheme encourages workers to save voluntarily for their retirement, offering a government-backed guaranteed minimum pension.",
        "benefits_text": "Subscribers receive a guaranteed minimum monthly pension of <strong>₹1,000, ₹2,000, ₹3,000, ₹4,000, or ₹5,000</strong> after attaining the age of 60, depending on their entry age and monthly contribution. In the event of the subscriber's death, the pension is paid to the spouse, and upon the death of both, the accumulated corpus is returned to the nominee.",
        "table_html": """<table>
          <thead>
            <tr>
              <th>Target Pension</th>
              <th>Monthly Premium (Entry Age 18)</th>
              <th>Monthly Premium (Entry Age 30)</th>
              <th>Monthly Premium (Entry Age 39)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>₹1,000 / month</td>
              <td>₹42</td>
              <td>₹116</td>
              <td>₹264</td>
            </tr>
            <tr>
              <td>₹2,000 / month</td>
              <td>₹84</td>
              <td>₹231</td>
              <td>₹528</td>
            </tr>
            <tr>
              <td>₹3,000 / month</td>
              <td>₹126</td>
              <td>₹347</td>
              <td>₹792</td>
            </tr>
            <tr>
              <td>₹5,000 / month</td>
              <td>₹210</td>
              <td>₹577</td>
              <td>₹1,318</td>
            </tr>
          </tbody>
        </table>""",
        "eligibility_list": [
            "The subscriber must be an Indian citizen.",
            "The entry age must be between 18 and 40 years.",
            "The subscriber must have an active savings bank account linked to a mobile number."
        ],
        "exclusions_list": [
            "Any citizen who is an income tax payer (effective from October 1, 2022).",
            "Subscribers covered under other statutory social security schemes (like EPFO, NPS, or Coal Mines Provident Fund)."
        ],
        "documents_list": [
            "<strong>Aadhaar Card:</strong> Proof of identity.",
            "<strong>Savings Bank Account Details:</strong> Mandatory for auto-debit of monthly/quarterly premiums."
        ],
        "apply_steps": [
            "Approach the bank branch where you maintain your savings account.",
            "Ask for the 'Atal Pension Yojana Proposal Form'.",
            "Select your desired monthly pension amount (₹1,000 – ₹5,000) and premium debit frequency (Monthly, Quarterly, or Half-yearly).",
            "Provide your spouse and nominee details.",
            "Consent to the auto-debit facility from your savings account.",
            "Submit the form. The bank will issue a PRAN (Permanent Retirement Account Number) card and register your account."
        ],
        "status_steps": [
            "Check APY transaction status online through the PFRDA APY CRA portal (cra-nsdl.com/RiaPRAN) using your PRAN number."
        ],
        "faqs": [
            {"q": "Can I exit the scheme before 60 years?", "a": "Voluntary premature exit before 60 is permitted only under exceptional circumstances like terminal illness or death of the subscriber, where the entire corpus is handed to the spouse/nominee."},
            {"q": "What happens if there is insufficient balance for auto-debit?", "a": "If auto-debit fails, a small penalty (ranging from ₹1 to ₹10 per month) is charged. If contributions stop completely, the account may be deactivated after 6 months and closed after 24 months."},
            {"q": "Are premiums tax-deductible?", "a": "Yes, contributions made to the Atal Pension Yojana are eligible for tax benefits under Section 80CCD (1B) of the Income Tax Act up to ₹50,000."}
        ]
    },
    # 12. PM Kaushal Vikas Yojana
    {
        "id": "pm-kaushal-vikas",
        "title": "PM Kaushal Vikas Yojana",
        "fullname": "Pradhan Mantri Kaushal Vikas Yojana (PMKVY) 4.0",
        "category": "education",
        "emoji": "🎓",
        "description": "Skill certification scheme offering free industry-relevant training, soft skills, and placement assistance for unemployed youth.",
        "meta_desc": "Explore PM Kaushal Vikas Yojana (PMKVY) 4.0. Details on skill training programs, courses, certificate value, eligibility, and online enrollment.",
        "meta_keywords": "PM Kaushal Vikas Yojana, PMKVY, Skill India, Free Skill Training, NSDC Courses, PMKVY Certificate",
        "intro": "<strong>Pradhan Mantri Kaushal Vikas Yojana (PMKVY)</strong> is the flagship skill training scheme of the Ministry of Skill Development & Entrepreneurship (MSDE), implemented by the National Skill Development Corporation (NSDC). Launched in 2015, the scheme is currently running its 4.0 phase. It aims to enable Indian youth to take up industry-relevant skill training, helping them secure better livelihoods through jobs or self-employment.",
        "benefits_text": "The scheme offers <strong>completely free skill training</strong> across hundreds of trades like IT, electronics, healthcare, retail, construction, and hospitality. Beneficiaries receive a certified Skill India certificate, assessment, digital literacy training, financial literacy support, soft skills coaching, and assistance in job placement.",
        "table_html": """<table>
          <thead>
            <tr>
              <th>Course Component</th>
              <th>Duration</th>
              <th>Certification</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Short Term Training (STT)</td>
              <td>200 – 600 hours (2-6 months)</td>
              <td>NSDC National Skills Qualification Framework (NSQF) Certificate</td>
            </tr>
            <tr>
              <td>Recognition of Prior Learning (RPL)</td>
              <td>12 – 80 hours (Upskilling/Assessment)</td>
              <td>Formal certification of existing informal skills</td>
            </tr>
            <tr>
              <td>Special Projects</td>
              <td>Variable (Customized for special demographics/areas)</td>
              <td>Industry-specific certifications</td>
            </tr>
          </tbody>
        </table>""",
        "eligibility_list": [
            "Any Indian citizen aged between 15 and 45 years.",
            "Unemployed youth, school dropouts, or college dropouts with a verifiable identity proof (Aadhaar).",
            "Candidates possessing an active bank account."
        ],
        "exclusions_list": [
            "Individuals currently pursuing full-time formal school or college education (except specialized vocational courses)."
        ],
        "documents_list": [
            "<strong>Aadhaar Card:</strong> Proof of identity and age.",
            "<strong>Educational Certificates:</strong> Class 10/12 marksheets (if applicable).",
            "<strong>Bank Passbook:</strong> For receiving training incentives/stipends."
        ],
        "apply_steps": [
            "Visit the official Skill India Digital portal at <strong>skillindiadigital.gov.in</strong>.",
            "Register as a student using your mobile number and complete the Aadhaar eKYC verification.",
            "Browse 'Skill Courses' and filter by your preferred sector, location, and language.",
            "Apply online for a course at your nearest PMKVY Training Centre (Pradhan Mantri Kaushal Kendra).",
            "Alternatively, visit a local Pradhan Mantri Kaushal Kendra (PMKK) center physically, speak with a counselor, and enroll in a batch."
        ],
        "status_steps": [
            "Log in to the Skill India Digital portal to track course progress, download course materials, check assessment schedules, and download your e-certificate."
        ],
        "faqs": [
            {"q": "Is there any stipend paid during the training?", "a": "Under specific short-term residential courses, boarding, lodging, and travel expenses are covered, and an incentive may be paid to the student's bank account upon passing the exam."},
            {"q": "Are PMKVY certificates valid internationally?", "a": "Yes, PMKVY certificates are issued under the National Skill Qualification Framework (NSQF), which is recognized by major industries and is highly valuable for international employment."},
            {"q": "Does PMKVY guarantee a job?", "a": "While it does not guarantee a job, PMKVY centers organize 'Rozgar Melas' (job fairs) and work with placement partners to assist successful candidates in securing placements."}
        ]
    },
    # 13. MGNREGA
    {
        "id": "mgnrega",
        "title": "MGNREGA Scheme",
        "fullname": "Mahatma Gandhi National Rural Employment Guarantee Act (MGNREGA)",
        "category": "employment",
        "emoji": "💼",
        "description": "Social security scheme guaranteeing 100 days of wage employment in a financial year to rural households.",
        "meta_desc": "Complete guide on MGNREGA. Learn about the 100-day job guarantee, wage rates, how to apply for a Job Card, and checking status online.",
        "meta_keywords": "MGNREGA, NREGA Job Card, Rural Employment Guarantee, NREGA Wage Rate, Job Card Apply",
        "intro": "The <strong>Mahatma Gandhi National Rural Employment Guarantee Act (MGNREGA)</strong> is a historical labor law and social security measure enacted in September 2005. The scheme guarantees <strong>100 days of wage employment</strong> in a financial year to rural households. It is designed to boost rural purchasing power and create durable local assets like roads, ponds, and canals.",
        "benefits_text": "Rural households receive guaranteed unskilled labor employment within 15 days of applying. Wages are paid directly into bank accounts based on state-specific wage rates. If employment is not provided within 15 days, applicants are entitled to receive an unemployment allowance.",
        "table_html": """<table>
          <thead>
            <tr>
              <th>Feature</th>
              <th>Guarantee / Details</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Guaranteed Employment</td>
              <td>100 days per rural household per financial year</td>
            </tr>
            <tr>
              <td>Wages Payment Mode</td>
              <td>Direct Benefit Transfer (DBT) to bank account</td>
            </tr>
            <tr>
              <td>Work Location</td>
              <td>Within 5 km radius of the village</td>
            </tr>
            <tr>
              <td>Unemployment Allowance</td>
              <td>Paid if work is not given within 15 days of demand</td>
            </tr>
          </tbody>
        </table>""",
        "eligibility_list": [
            "The applicant must be a resident of a rural area in India.",
            "The applicant must be an adult member of the rural household (aged 18 or above).",
            "The applicant must volunteer for unskilled manual labor."
        ],
        "exclusions_list": [
            "Urban residents.",
            "Minor children (aged below 18).",
            "Skilled/professional work seekers (the scheme covers only unskilled manual labor)."
        ],
        "documents_list": [
            "<strong>Aadhaar Card:</strong> For biometric registration.",
            "<strong>Proof of Residence:</strong> Voter ID, ration card, or gram panchayat verification.",
            "<strong>Bank Account Details:</strong> Linked with Aadhaar for receiving wages."
        ],
        "apply_steps": [
            "Approach your local Gram Panchayat office in your village.",
            "Request a 'Job Card Application Form' (Form 1).",
            "Fill in the household details and names of adult family members willing to work.",
            "Attach passport-size photos and a copy of your Aadhaar card.",
            "Submit the form to the Gram Panchayat. The Panchayat will verify details and issue an official **NREGA Job Card** within 15 days.",
            "Once you have the Job Card, submit a written request for work to the Gram Panchayat."
        ],
        "status_steps": [
            "Visit the official NREGA portal at <strong>nrega.nic.in</strong>.",
            "Select your State, District, Block, and Gram Panchayat.",
            "Click on 'Job Card' to view the household job card details, work history, and payment status."
        ],
        "faqs": [
            {"q": "What is the current wage rate under MGNREGA?", "a": "Wages vary by state, ranging from approximately ₹230 to ₹370 per day, adjusted annually by the Central Government based on the Consumer Price Index (CPI-AL)."},
            {"q": "How is the work allocated?", "a": "Work is allocated on local assets like water conservation projects, afforestation, rural connectivity, land development, and sanitation infrastructure within the village."},
            {"q": "Is there a reservation for women under MGNREGA?", "a": "Yes, the Act mandates that at least one-third (33%) of the beneficiaries must be women."}
        ]
    },
    # 14. Startup India
    {
        "id": "startup-india",
        "title": "Startup India Scheme",
        "fullname": "Startup India Initiative 2026",
        "category": "employment",
        "emoji": "🚀",
        "description": "Government initiative supporting entrepreneurs with tax exemptions, funding opportunities, and fast-track patent filing.",
        "meta_desc": "Complete information on the Startup India scheme. Find DPIIT recognition steps, tax benefits, seed fund details, and online registration.",
        "meta_keywords": "Startup India, DPIIT Recognition, Startup Seed Fund, Startup Tax Exemption, Register Startup",
        "intro": "The <strong>Startup India Initiative</strong> was launched by Prime Minister Narendra Modi on January 16, 2016. Managed by the Department for Promotion of Industry and Internal Trade (DPIIT), the scheme is designed to build a strong ecosystem for nurturing innovation and startups in India, driving sustainable economic growth and generating large-scale employment opportunities.",
        "benefits_text": "Registered startups receive a wide range of benefits including a 3-year income tax holiday, 80% rebate on patent filing costs, simplified compliance self-certification, access to a ₹10,000 crore Fund of Funds, and eligibility to apply for the Startup India Seed Fund Scheme (SISFS) offering grants up to ₹20 lakh.",
        "table_html": """<table>
          <thead>
            <tr>
              <th>Benefit Area</th>
              <th>Support Provided</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Tax Holidays</td>
              <td>100% income tax exemption for 3 consecutive years out of the first 10 years of operations</td>
            </tr>
            <tr>
              <td>Patent Fast-tracking</td>
              <td>80% rebate on patent filing and 50% rebate on trademark applications</td>
            </tr>
            <tr>
              <td>Seed Funding</td>
              <td>Grants up to ₹20 Lakh for proof of concept, and loans up to ₹50 Lakh for commercialization</td>
            </tr>
            <tr>
              <td>Procurement</td>
              <td>Exemption from prior experience and earnest money deposit (EMD) in government tenders</td>
            </tr>
          </tbody>
        </table>""",
        "eligibility_list": [
            "The entity must be registered as a Private Limited Company, Partnership Firm, or Limited Liability Partnership (LLP) in India.",
            "The incorporation period must not exceed 10 years from the date of registration.",
            "The annual turnover must not exceed ₹100 crore in any of the financial years since incorporation.",
            "The startup must be working towards innovation, development, or improvement of products, processes, or services."
        ],
        "exclusions_list": [
            "Sole proprietorships.",
            "Entities formed by splitting up or reconstructing an existing business."
        ],
        "documents_list": [
            "<strong>Certificate of Incorporation/Registration:</strong> Issued by MCA/Registrar of Firms.",
            "<strong>Proof of Concept/Pitch Deck:</strong> Explaining the innovative nature of the startup.",
            "<strong>PAN Card of the Entity:</strong> Tax identification number."
        ],
        "apply_steps": [
            "Visit the official portal at <strong>startupindia.gov.in</strong>.",
            "Click on 'Register' and enter your basic details to create an account.",
            "Go to the 'DPIIT Recognition' page and click 'Apply for Recognition'.",
            "Fill in the online form, providing incorporation details, website/app link, and details of directors/partners.",
            "Upload the certificate of incorporation and submit the application.",
            "DPIIT will review the application and issue a 'Certificate of Recognition' within 5-7 working days if eligible."
        ],
        "status_steps": [
            "Log in to <strong>startupindia.gov.in</strong> and view the dashboard to check the status of your DPIIT recognition certificate."
        ],
        "faqs": [
            {"q": "What is the Startup India Seed Fund Scheme?", "a": "It is a scheme providing financial assistance to early-stage startups for product trials, prototype development, market entry, and commercialization through selected incubator networks."},
            {"q": "How can I get the 3-year tax exemption?", "a": "DPIIT-recognized startups must submit a separate application to the Inter-Ministerial Board (IMB) through the Startup India portal to qualify for the Section 80-IAC tax holiday."}
        ]
    },
    # 15. PM Fasal Bima
    {
        "id": "pm-fasal-bima",
        "title": "PM Fasal Bima Yojana",
        "fullname": "Pradhan Mantri Fasal Bima Yojana (PMFBY)",
        "category": "agriculture",
        "emoji": "🌾",
        "description": "Comprehensive crop insurance scheme offering low-premium insurance cover for crops against natural calamities.",
        "meta_desc": "Learn about PM Fasal Bima Yojana (PMFBY). Crop insurance premium rates, coverage against natural disasters, and online claim/application process.",
        "meta_keywords": "PM Fasal Bima Yojana, PMFBY, Crop Insurance Scheme, Farmer Insurance, Agriculture Calamity Claim",
        "intro": "The <strong>Pradhan Mantri Fasal Bima Yojana (PMFBY)</strong> was launched by Prime Minister Narendra Modi on February 18, 2016. It is an actuarial premium-based crop insurance scheme designed to provide financial support to farmers experiencing crop loss or damage arising out of unforeseen natural events like drought, floods, pests, and landslides, stabilizing farmer incomes.",
        "benefits_text": "Farmers are charged a highly subsidized uniform premium of only 2% for Kharif crops, 1.5% for Rabi crops, and 5% for annual commercial/horticultural crops. The remaining premium balance is shared equally between the Central and State Governments.",
        "table_html": """<table>
          <thead>
            <tr>
              <th>Crop Category</th>
              <th>Season</th>
              <th>Farmer Share of Premium</th>
              <th>Government Subsidy Share</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Foodgrains &amp; Oilseeds</td>
              <td>Kharif</td>
              <td>2.0%</td>
              <td>Balance Premium</td>
            </tr>
            <tr>
              <td>Foodgrains &amp; Oilseeds</td>
              <td>Rabi</td>
              <td>1.5%</td>
              <td>Balance Premium</td>
            </tr>
            <tr>
              <td>Commercial / Horticultural</td>
              <td>Annual</td>
              <td>5.0%</td>
              <td>Balance Premium</td>
            </tr>
          </tbody>
        </table>""",
        "eligibility_list": [
            "All farmers, including sharecroppers and tenant farmers, growing notified crops in notified areas.",
            "The scheme is optional for all farmers."
        ],
        "exclusions_list": [
            "Crops damaged due to preventable factors, theft, or war/nuclear risks.",
            "Crops grown in non-notified areas."
        ],
        "documents_list": [
            "<strong>Aadhaar Card:</strong> Proof of identity.",
            "<strong>Land Ownership Papers:</strong> Or tenancy agreement if tenant farmer.",
            "<strong>Sowing Certificate:</strong> Issued by the local Patwari/agriculture officer.",
            "<strong>Bank Account Passbook:</strong> Linked with Aadhaar for direct claim settlement."
        ],
        "apply_steps": [
            "Visit the official PMFBY portal at <strong>pmfby.gov.in</strong>.",
            "Click on 'Farmer Corner' and register/log in using your mobile number.",
            "Fill in your crop and land details, selecting the correct notified area and crop season.",
            "Upload the Land registration document, sowing certificate, and bank passbook copy.",
            "Pay the applicable subsidized premium online.",
            "Alternatively, apply offline through your lending bank (where you have a Kisan Credit Card account) or CSC centers."
        ],
        "status_steps": [
            "Go to <strong>pmfby.gov.in</strong> and click on 'Application Status' to check the verification and approval of your crop insurance policy."
        ],
        "faqs": [
            {"q": "How to report crop loss?", "a": "Crop loss must be reported within 72 hours of the occurrence of natural disaster through the 'Crop Insurance App', the PMFBY portal, or by notifying your insurance company or local agriculture office."},
            {"q": "What disasters are covered under PMFBY?", "a": "Prevented sowing, mid-season adversity, standing crop damage (due to dry spells, drought, floods, pests), and post-harvest losses up to 14 days are covered."}
        ]
    },
    # 16. Kisan Credit Card
    {
        "id": "kisan-credit-card",
        "title": "Kisan Credit Card Scheme",
        "fullname": "Kisan Credit Card (KCC) Scheme 2026",
        "category": "agriculture",
        "emoji": "💳",
        "description": "Subsidized short-term credit scheme for farmers to purchase seeds, fertilizers, and agricultural equipment.",
        "meta_desc": "Complete guide on Kisan Credit Card (KCC). Check credit limits, interest rates, subvention schemes, eligibility, and bank application process.",
        "meta_keywords": "Kisan Credit Card, KCC Loan, Subsidized Farmer Loan, Crop Loan, KCC Interest Subvention",
        "intro": "The <strong>Kisan Credit Card (KCC)</strong> scheme was introduced in August 1998 by Indian banks based on the recommendations of the R.V. Gupta Committee. In 2026, it remains a critical credit facility, providing farmers with timely access to affordable credit for agricultural inputs, crop cultivation, post-harvest expenses, and allied activities like animal husbandry and fisheries.",
        "benefits_text": "KCC provides short-term credit at a nominal interest rate. While the nominal rate is 9%, the Government of India provides an <strong>interest subvention of 2%</strong>, and an additional <strong>3% prompt repayment incentive</strong>, bringing the effective interest rate down to just <strong>4% per annum</strong> for loans up to ₹3 lakh.",
        "table_html": """<table>
          <thead>
            <tr>
              <th>Loan Component</th>
              <th>Details &amp; Limits</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Effective Interest Rate</td>
              <td>4.0% per annum (with prompt repayment of loans up to ₹3 Lakh)</td>
            </tr>
            <tr>
              <td>Card Validity</td>
              <td>5 years (with automatic annual renewal based on performance)</td>
            </tr>
            <tr>
              <td>Insurance Coverage</td>
              <td>Accidental death/permanent disability cover up to ₹50,000</td>
            </tr>
            <tr>
              <td>Allied Limits</td>
              <td>Up to ₹2 Lakh for Animal Husbandry &amp; Fisheries within the ₹3 Lakh limit</td>
            </tr>
          </tbody>
        </table>""",
        "eligibility_list": [
            "All owner-cultivator farmers.",
            "Tenant farmers, oral lessees, and sharecroppers.",
            "Self-Help Groups (SHGs) or Joint Liability Groups (JLGs) of farmers.",
            "Fishermen, dairy farmers, and poultry owners."
        ],
        "exclusions_list": [
            "Individuals with zero involvement in agricultural or allied activities.",
            "Applicants with a default history with any lending institution."
        ],
        "documents_list": [
            "<strong>Aadhaar Card:</strong> Proof of identity.",
            "<strong>Land Revenue Record:</strong> Proving land ownership/cultivation area.",
            "<strong>Crop Sowing Certificate:</strong> Declaring planned crops."
        ],
        "apply_steps": [
            "Visit the bank branch where you have your savings account.",
            "Fill in the Kisan Credit Card application form, declaring your land holding and sowed crops.",
            "Attach photocopies of land records and Aadhaar card.",
            "The bank officer will verify your land ownership and credit score.",
            "Upon approval, the bank will issue the Kisan Credit Card."
        ],
        "status_steps": [
            "Subscribers can check the status of their KCC application directly by visiting their local bank branch or accessing online banking panels."
        ],
        "faqs": [
            {"q": "Is collateral security mandatory for KCC?", "a": "No. Collateral security has been waived for KCC loans up to ₹1.6 lakh."},
            {"q": "How can I withdraw money from KCC?", "a": "You can withdraw funds using your KCC RuPay card at any ATM, POS machine, or bank branch."}
        ]
    },
    # 17. Beti Bachao Beti Padhao
    {
        "id": "beti-bachao",
        "title": "Beti Bachao Beti Padhao",
        "fullname": "Beti Bachao Beti Padhao (BBBP) Campaign",
        "category": "women",
        "emoji": "👩‍👧",
        "description": "National campaign to address gender bias, ensure survival of the girl child, and support girl child education.",
        "meta_desc": "Understand the objectives of Beti Bachao Beti Padhao (BBBP). Details on scheme implementation, girl child education support, and key benefits.",
        "meta_keywords": "Beti Bachao Beti Padhao, BBBP, Girl Child Protection, Girl Child Education, Beti Padhao Scheme",
        "intro": "<strong>Beti Bachao Beti Padhao (BBBP)</strong> was launched by Prime Minister Narendra Modi on January 22, 2015. It is a joint initiative of the Ministry of Women and Child Development, Ministry of Health and Family Welfare, and Ministry of Education. The scheme aims to address the declining Child Sex Ratio (CSR) and resolve issues related to women empowerment, survival, and education of girls.",
        "benefits_text": "Rather than a direct cash transfer scheme, BBBP is an advocacy campaign combined with multi-sectoral action. It ensures survival and protection of the girl child, eliminates sex-selective abortion, promotes girl education (including building separate toilets in schools), and works closely with savings schemes like Sukanya Samriddhi Yojana.",
        "table_html": """<table>
          <thead>
            <tr>
              <th>Focus Area</th>
              <th>Action Taken</th>
              <th>Target Outcome</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Prevention of Gender Bias</td>
              <td>Strict enforcement of PC-PNDT Act (anti-sex determination)</td>
              <td>Improve Child Sex Ratio at birth</td>
            </tr>
            <tr>
              <td>Girl Child Survival</td>
              <td>Promote institutional deliveries and nutrition programs</td>
              <td>Reduce infant mortality rates in girls</td>
            </tr>
            <tr>
              <td>Education &amp; Safety</td>
              <td>Ensure girl-friendly school infrastructure and zero dropouts</td>
              <td>Universal secondary education for girls</td>
            </tr>
          </tbody>
        </table>""",
        "eligibility_list": [
            "All Indian families with a girl child, with campaigns focused primarily on districts with a low Child Sex Ratio.",
            "All girl children studying in government or recognized private schools."
        ],
        "exclusions_list": [
            "None. The scheme campaigns and policy supports are applicable universally across all Indian districts."
        ],
        "documents_list": [
            "<strong>No direct registration needed:</strong> This is a public policy campaign. However, to benefit from linked schemes (like Sukanya Samriddhi Yojana), standard documents like Birth Certificate and Guardian Aadhaar are needed."
        ],
        "apply_steps": [
            "As BBBP is a national social campaign, families do not apply to it directly.",
            "To participate or secure benefits, enroll your girl child in nearby government schools where fee waivers, free uniforms, and cycles are provided.",
            "Open a Sukanya Samriddhi Yojana account at the nearest post office."
        ],
        "status_steps": [
            "Information about local camp events, scholarships, and initiatives under BBBP can be verified via your local Gram Panchayat or District Magistrate's office."
        ],
        "faqs": [
            {"q": "Does Beti Bachao Beti Padhao offer direct cash payouts?", "a": "No. Beware of fraud. The government does not distribute direct cash to individuals under BBBP. The funds are utilized for school construction, public awareness, girl child healthcare, and district-level welfare infrastructure."},
            {"q": "What is the primary goal of the BBBP scheme?", "a": "The primary goal is to prevent gender-biased sex-selective elimination, ensure survival and protection of the girl child, and facilitate her education."}
        ]
    },
    # 18. PM Jeevan Jyoti
    {
        "id": "pm-jeevan-jyoti",
        "title": "PM Jeevan Jyoti Bima Yojana",
        "fullname": "Pradhan Mantri Jeevan Jyoti Bima Yojana (PMJJBY)",
        "category": "finance",
        "emoji": "🛡️",
        "description": "Low-premium government life insurance scheme offering ₹2 lakh cover at an annual premium of ₹436.",
        "meta_desc": "Learn about Pradhan Mantri Jeevan Jyoti Bima Yojana (PMJJBY). Premium details, ₹2 lakh life insurance cover, eligibility, and claim settlement process.",
        "meta_keywords": "PM Jeevan Jyoti Bima Yojana, PMJJBY, Low Premium Life Insurance, Government Insurance Scheme, ₹2 Lakh Life Cover",
        "intro": "<strong>Pradhan Mantri Jeevan Jyoti Bima Yojana (PMJJBY)</strong> is a government-backed life insurance scheme in India, launched on May 9, 2015, by PM Narendra Modi. It is designed to increase life insurance penetration among low-income populations and unorganized sector workers, providing substantial financial security to their families in the event of the subscriber's untimely demise.",
        "benefits_text": "PMJJBY offers a <strong>one-year renewable life insurance cover of ₹2,00,000 (₹2 Lakh)</strong> to the subscriber. The cover is payable to the nominee upon the death of the subscriber due to any reason. The annual premium is a highly affordable <strong>₹436</strong>, auto-debited from the bank account.",
        "table_html": """<table>
          <thead>
            <tr>
              <th>Feature</th>
              <th>Details</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Insurance Cover Limit</td>
              <td>₹2 Lakh (payable to nominee in case of death due to any cause)</td>
            </tr>
            <tr>
              <td>Annual Premium</td>
              <td>₹436 per year</td>
            </tr>
            <tr>
              <td>Payment Mode</td>
              <td>Auto-debit from savings bank account</td>
            </tr>
            <tr>
              <td>Insurance Period</td>
              <td>June 1 to May 31 (Renewable annually)</td>
            </tr>
          </tbody>
        </table>""",
        "eligibility_list": [
            "The subscriber must be an Indian citizen.",
            "The entry age must be between 18 and 50 years.",
            "The subscriber must have an active savings bank account.",
            "Consent to auto-debit of the premium amount from the linked savings account."
        ],
        "exclusions_list": [
            "Individuals aged below 18 or above 50 (though coverage continues up to age 55 if enrolled before 50)."
        ],
        "documents_list": [
            "<strong>Aadhaar Card:</strong> Proof of identity.",
            "<strong>Savings Bank Account Details:</strong> Linked with mobile number for auto-debit consent."
        ],
        "apply_steps": [
            "Approach the bank branch or post office where you maintain your savings account.",
            "Ask for the 'PMJJBY Consent-cum-Declaration Form'.",
            "Fill in your personal details, Aadhaar number, and designate a nominee.",
            "Check the box giving consent for auto-debit of ₹436 annually.",
            "Submit the form. Alternatively, activate it instantly via Net Banking or Mobile Banking."
        ],
        "status_steps": [
            "Verify registration by checking your bank passbook/statement for the debit of ₹436 around June 1 every year."
        ],
        "faqs": [
            {"q": "Can I link multiple bank accounts for PMJJBY?", "a": "No. A person can enroll in PMJJBY through only one bank account, regardless of having accounts in multiple banks. Multiple enrollments will render the claims invalid."},
            {"q": "What is the lien period under PMJJBY?", "a": "There is a lien period of 30 days from the date of enrollment, during which risk cover is not available. Demise due to accidents is, however, covered from day one."}
        ]
    },
    # 19. PM Suraksha Bima
    {
        "id": "pm-suraksha-bima",
        "title": "PM Suraksha Bima Yojana",
        "fullname": "Pradhan Mantri Suraksha Bima Yojana (PMSBY)",
        "category": "finance",
        "emoji": "🛡️",
        "description": "Low-premium personal accident insurance scheme offering up to ₹2 lakh cover at an annual premium of ₹20.",
        "meta_desc": "Check details of Pradhan Mantri Suraksha Bima Yojana (PMSBY). Find accidental insurance coverage, ₹20 annual premium, eligibility, and claim steps.",
        "meta_keywords": "PM Suraksha Bima Yojana, PMSBY, Accidental Insurance Scheme, Low Cost Insurance, ₹20 Premium Insurance",
        "intro": "<strong>Pradhan Mantri Suraksha Bima Yojana (PMSBY)</strong> was launched alongside PMJJBY on May 9, 2015. It is a government-backed accident insurance scheme, aiming to provide financial protection against accidental death and permanent disability, offering a safety net to families at an exceptionally low premium.",
        "benefits_text": "PMSBY offers an accident insurance cover of <strong>₹2,00,000 (₹2 Lakh)</strong> in case of accidental death or total permanent disability. A cover of <strong>₹1,00,000 (₹1 Lakh)</strong> is provided for partial permanent disability. The annual premium is just <strong>₹20</strong>, debited automatically from the subscriber's bank account.",
        "table_html": """<table>
          <thead>
            <tr>
              <th>Accident Event</th>
              <th>Insurance Claim Cover</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Accidental Death</td>
              <td>₹2,00,000 (₹2 Lakh)</td>
            </tr>
            <tr>
              <td>Total and Irrecoverable Loss of Both Eyes/Hands/Feet</td>
              <td>₹2,00,000 (₹2 Lakh)</td>
            </tr>
            <tr>
              <td>Total and Irrecoverable Loss of One Eye/Hand/Foot</td>
              <td>₹1,00,000 (₹1 Lakh)</td>
            </tr>
            <tr>
              <td>Annual Premium Cost</td>
              <td>₹20 (Renewable annually via auto-debit)</td>
            </tr>
          </tbody>
        </table>""",
        "eligibility_list": [
            "The subscriber must be an Indian citizen.",
            "The entry age must be between 18 and 70 years.",
            "The subscriber must have an active savings bank account.",
            "Provide consent to auto-debit of the premium from the savings account."
        ],
        "exclusions_list": [
            "Individuals aged below 18 or above 70 years.",
            "Deaths due to suicide are not covered."
        ],
        "documents_list": [
            "<strong>Aadhaar Card:</strong> Proof of identity.",
            "<strong>Savings Bank Account Passbook:</strong> Linked with Aadhaar for auto-debit."
        ],
        "apply_steps": [
            "Visit the bank branch or post office holding your savings account.",
            "Fill in the 'PMSBY Consent-cum-Declaration Form'.",
            "Provide nominee details and authorize the bank to auto-debit ₹20 annually.",
            "Submit the form. Alternatively, activate the policy through Net Banking."
        ],
        "status_steps": [
            "Monitor your bank statement for a debit of ₹20 under the head 'PMSBY' in May/June of every year."
        ],
        "faqs": [
            {"q": "Are natural deaths covered under PMSBY?", "a": "No. PMSBY only covers deaths and disabilities resulting from accidents. For natural deaths, see PMJJBY."},
            {"q": "How to claim insurance under PMSBY?", "a": "The nominee must submit a claim form to the bank branch holding the account within 30 days of the accident, attaching the FIR and Death Certificate."}
        ]
    },
    # 20. Swachh Bharat Mission
    {
        "id": "swachh-bharat",
        "title": "Swachh Bharat Mission",
        "fullname": "Swachh Bharat Mission (SBM) Gramin and Urban",
        "category": "housing",
        "emoji": "🧹",
        "description": "Cleanliness campaign offering financial incentive of ₹12,000 for constructing individual household latrines in rural areas.",
        "meta_desc": "Complete details of Swachh Bharat Mission toilet subsidy. Find eligibility, ₹12,000 toilet incentive, and online application process.",
        "meta_keywords": "Swachh Bharat Mission, SBM Toilet Subsidy, Toilet Construction Incentive, SBM Rural, Clean India Scheme",
        "intro": "<strong>Swachh Bharat Mission (SBM)</strong> was launched by PM Narendra Modi on October 2, 2014. SBM has two arms: SBM-Gramin and SBM-Urban. The main objective was to make India 100% Open Defecation Free (ODF) through building household toilets.",
        "benefits_text": "Eligible households receive a direct financial incentive of <strong>₹12,000</strong> to construct an Individual Household Latrine (IHHL). The incentive is released directly to the beneficiary's bank account in installments upon verification of toilet construction phases.",
        "table_html": """<table>
          <thead>
            <tr>
              <th>Beneficiary Category</th>
              <th>Subsidy Incentive</th>
              <th>Funding Split (Center/State)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Rural Households (BPL/APL-SC/ST)</td>
              <td>₹12,000</td>
              <td>60:40 (Plains) | 90:10 (Hilly regions)</td>
            </tr>
            <tr>
              <td>Urban Households (LIG/EWS)</td>
              <td>Varies by State/Municipal Corporation</td>
              <td>Shared contribution</td>
            </tr>
          </tbody>
        </table>""",
        "eligibility_list": [
            "The household must not have any existing toilet.",
            "Rural households listed under BPL (Below Poverty Line) list.",
            "Identified APL (Above Poverty Line) rural households belonging to SC/ST, small & marginal farmers, landless laborers, women-headed households, and physically disabled individuals."
        ],
        "exclusions_list": [
            "Households that already possess a functional toilet or have previously received a government toilet construction subsidy."
        ],
        "documents_list": [
            "<strong>Aadhaar Card:</strong> Proof of identity.",
            "<strong>Bank Account Details:</strong> Bank passbook copy showing IFSC code.",
            "<strong>Photograph:</strong> Photograph of the applicant standing in front of the site before and after toilet construction."
        ],
        "apply_steps": [
            "Visit the official SBM-Gramin portal at <strong>sbm.gov.in/sbm_dbt</strong>.",
            "Register as a citizen and log in using your registered mobile number and OTP.",
            "Click on 'New Application (IHHL)' and fill in your state, district, block, and panchayat details.",
            "Enter the applicant's name as per Aadhaar and bank details.",
            "Submit the application. A village sanitation inspector will visit your site to verify.",
            "Once approved, construct the toilet structure and upload photos of the completed toilet."
        ],
        "status_steps": [
            "Log in to the citizen portal <strong>sbm.gov.in/sbm_dbt</strong> and click 'Track Application Status' to view sanitation inspector approvals and payment release status."
        ],
        "faqs": [
            {"q": "What is the recommended toilet design under SBM?", "a": "The twin-pit pour-flush toilet is recommended as it is cheap, easy to build, and converts human waste into organic compost naturally."},
            {"q": "Can urban citizens apply online for toilet subsidy?", "a": "Yes, urban citizens can apply through the SBM-Urban portal or approach their local municipal corporation office."}
        ]
    },
    # 21. PM Matru Vandana (Maternity Benefit)
    {
        "id": "maternity-benefit",
        "title": "PM Matru Vandana Yojana",
        "fullname": "Pradhan Mantri Matru Vandana Yojana (PMMVY)",
        "category": "women",
        "emoji": "🤰",
        "description": "Maternity benefit scheme offering ₹5,000 cash incentive to pregnant and lactating mothers for the first living child.",
        "meta_desc": "Complete guide on PM Matru Vandana Yojana (PMMVY). Check eligibility, ₹5000 maternity benefit installments, and online application process.",
        "meta_keywords": "PM Matru Vandana Yojana, PMMVY, Maternity Benefit Scheme, Pregnant Women Subsidy, Women Health Scheme",
        "intro": "<strong>Pradhan Mantri Matru Vandana Yojana (PMMVY)</strong> is a maternity benefit program run by the Ministry of Women and Child Development, Government of India. Launched on January 1, 2017, the scheme provides cash incentives to pregnant women and lactating mothers to compensate for wage loss during childbirth, encouraging institutional deliveries and vaccination.",
        "benefits_text": "Beneficiaries receive a total cash benefit of <strong>₹5,000</strong> in two installments for the first child. An additional amount of <strong>₹6,000</strong> is provided under updated guidelines if the second child is a girl, supporting the girl child ratio.",
        "table_html": """<table>
          <thead>
            <tr>
              <th>Installment (First Child)</th>
              <th>Conditions to be Met</th>
              <th>Amount</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>1st Installment</td>
              <td>Early registration of pregnancy (within 150 days of LMP) + at least 1 Antenatal Check-up (ANC)</td>
              <td>₹3,000</td>
            </tr>
            <tr>
              <td>2nd Installment</td>
              <td>Child birth registration + BCG, OPV, DPT, and Hepatitis-B vaccinations</td>
              <td>₹2,000</td>
            </tr>
          </tbody>
        </table>""",
        "eligibility_list": [
            "All Pregnant Women and Lactating Mothers (PW&LM) who have registered their pregnancy for the first child.",
            "The pregnancy must be registered at a government-approved health facility."
        ],
        "exclusions_list": [
            "Women in regular employment with the Central Government, State Governments, or PSUs.",
            "Women who are in receipt of similar benefits under any other maternity benefit law."
        ],
        "documents_list": [
            "<strong>Mother and Child Protection (MCP) Card:</strong> Mandatory showing ANC details and vaccinations.",
            "<strong>Aadhaar Card:</strong> Of the applicant.",
            "<strong>Bank Passbook:</strong> For Direct Benefit Transfer (DBT).",
            "<strong>Child Birth Certificate:</strong> Mandatory for claiming the final installment."
        ],
        "apply_steps": [
            "Register your pregnancy at the nearest Anganwadi Centre (AWC) or Government Health Centre.",
            "Request the PMMVY Form 1A from the Anganwadi Worker or download from the portal.",
            "Fill in details and submit to the Anganwadi Worker.",
            "After child birth and vaccination, submit Form 1B along with the birth certificate and MCP card copy for the second installment.",
            "Alternatively, apply online directly through the citizen login portal at <strong>pmmvy.wcd.gov.in</strong>."
        ],
        "status_steps": [
            "Log in to <strong>pmmvy.wcd.gov.in</strong> with your registered mobile number and click on 'Track Application Status' to monitor approvals."
        ],
        "faqs": [
            {"q": "Can I claim benefits for a second child?", "a": "Under the new guidelines, benefits are extended to the second child only if the second child born is a girl child, in which case a single installment of ₹6,000 is paid."},
            {"q": "What happens in case of miscarriage?", "a": "If a beneficiary experiences miscarriage, she remains eligible to claim the remaining installments in her future pregnancy."}
        ]
    },
    # 22. PM Shram Yogi Maan-dhan
    {
        "id": "pm-shram-yogi",
        "title": "PM Shram Yogi Maan-Dhan",
        "fullname": "Pradhan Mantri Shram Yogi Maan-Dhan (PM-SYM)",
        "category": "pension",
        "emoji": "💼",
        "description": "Voluntary pension scheme for unorganized workers offering guaranteed pension of ₹3,000/month after age 60.",
        "meta_desc": "Complete guide on PM Shram Yogi Maan-Dhan (PM-SYM) pension scheme. Premium rates, eligibility, and online registration steps.",
        "meta_keywords": "PM Shram Yogi Maan-dhan, PMSYM Pension, Unorganized Sector Pension, PMSYM Premium Table, Pension Scheme",
        "intro": "<strong>Pradhan Mantri Shram Yogi Maan-Dhan (PM-SYM)</strong> is a voluntary and contributory pension scheme launched in February 2019 by the Ministry of Labour and Employment, Government of India. The scheme is aimed at securing old age social security for unorganized workers like street vendors, rickshaw pullers, brick kiln workers, and ragpickers.",
        "benefits_text": "Subscribers receive a guaranteed minimum monthly pension of <strong>₹3,000</strong> after attaining the age of 60. The scheme is a 50:50 contributory scheme where the subscriber contributes a monthly premium, and the Central Government makes an equal matching contribution.",
        "table_html": """<table>
          <thead>
            <tr>
              <th>Entry Age</th>
              <th>Subscriber Monthly Contribution</th>
              <th>Government Matching Contribution</th>
              <th>Total Monthly Pension Fund</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>18 Years</td>
              <td>₹55</td>
              <td>₹55</td>
              <td>₹110</td>
            </tr>
            <tr>
              <td>25 Years</td>
              <td>₹80</td>
              <td>₹80</td>
              <td>₹160</td>
            </tr>
            <tr>
              <td>30 Years</td>
              <td>₹105</td>
              <td>₹105</td>
              <td>₹210</td>
            </tr>
            <tr>
              <td>40 Years (Max Age)</td>
              <td>₹200</td>
              <td>₹200</td>
              <td>₹400</td>
            </tr>
          </tbody>
        </table>""",
        "eligibility_list": [
            "The applicant must be a resident of India.",
            "The applicant must be working in the unorganized sector.",
            "The entry age must be between 18 and 40 years.",
            "The monthly income of the applicant must be ₹15,000 or less."
        ],
        "exclusions_list": [
            "Workers covered under organized sectors (EPFO, ESIC, or NPS).",
            "Income tax payers."
        ],
        "documents_list": [
            "<strong>Aadhaar Card:</strong> Proof of identity and age.",
            "<strong>Savings Bank Account Details:</strong> Passbook copy showing IFSC for auto-debit."
        ],
        "apply_steps": [
            "Visit the nearest Common Service Centre (CSC) or register online at <strong>maandhan.in</strong>.",
            "Log in using your mobile number and click on 'Services' -> 'Enrollment'.",
            "Enter your Aadhaar, name, and DOB to verify details.",
            "Enter your bank account number, IFSC code, and select monthly premium auto-debit authorization.",
            "The portal will generate a customized 'Shram Yogi Pension Card'."
        ],
        "status_steps": [
            "Subscribers can check their premium payment ledger and account details online at <strong>maandhan.in</strong> using their SPAN or mobile number."
        ],
        "faqs": [
            {"q": "What happens if a subscriber dies before 60?", "a": "If a subscriber dies before 60, their spouse is entitled to continue the scheme by paying regular premiums, or exit and claim the accumulated fund with bank interest."},
            {"q": "Is the pension taxable?", "a": "The pension payouts of ₹3,000 per month are subject to tax guidelines in the future, though generally exempt for low-income brackets."}
        ]
    }
]

# Write Javascript logic to handle dropdown search filter & updates
def update_script():
    js_file = "c:\\Users\\durga\\OneDrive\\Desktop\\yojana\\script.js"
    content = ""
    if os.path.exists(js_file):
        with open(js_file, "r") as f:
            content = f.read()
    
    if "/* ---------- Dropdown menu on mobile ---------- */" not in content:
        extra_js = """
  /* ---------- Dropdown menu on mobile ---------- */
  const dropdownToggle = document.querySelector('.dropdown-toggle');
  if (dropdownToggle) {
    dropdownToggle.addEventListener('click', function (e) {
      if (window.innerWidth <= 768) {
        e.preventDefault();
        const dropdownMenu = this.nextElementSibling;
        dropdownMenu.classList.toggle('show');
        const arrow = this.querySelector('.arrow');
        if (arrow) {
          arrow.style.transform = dropdownMenu.classList.contains('show') ? 'rotate(180deg)' : '';
        }
      }
    });
  }
"""
        with open(js_file, "a") as f:
            f.write(extra_js)
        print("Updated script.js with mobile dropdown logic.")

# Update CSS for Dropdown Menu styling
def update_css():
    css_file = "c:\\Users\\durga\\OneDrive\\Desktop\\yojana\\styles.css"
    content = ""
    if os.path.exists(css_file):
        with open(css_file, "r") as f:
            content = f.read()
            
    if "/* Dropdown Container */" not in content:
        dropdown_css = """
/* ---------- Navigation Dropdown Menu ---------- */
/* Dropdown Container */
.nav-list li {
  position: relative;
}

/* Dropdown Toggle Arrow */
.nav-list li.dropdown .arrow {
  font-size: 0.7rem;
  margin-left: 4px;
  display: inline-block;
  transition: transform var(--transition-fast);
}

.nav-list li.dropdown:hover .arrow {
  transform: rotate(180deg);
}

/* Dropdown Menu Styles */
.dropdown-menu {
  position: absolute;
  top: 100%;
  left: 50%;
  transform: translateX(-50%) translateY(10px);
  background: var(--royal-blue);
  min-width: 250px;
  border-radius: 8px;
  box-shadow: var(--shadow-xl);
  padding: 0.5rem 0;
  opacity: 0;
  visibility: hidden;
  transition: all var(--transition-normal);
  list-style: none;
  border: 1px solid rgba(255, 255, 255, 0.1);
  max-height: 380px;
  overflow-y: auto;
  z-index: 1001;
}

.dropdown-menu li {
  width: 100%;
}

.dropdown-menu li a {
  display: block;
  padding: 0.6rem 1.25rem !important;
  color: rgba(255, 255, 255, 0.9) !important;
  font-weight: 450 !important;
  font-size: 0.88rem !important;
  border-radius: 0 !important;
  background: transparent !important;
  text-align: left;
  transition: all var(--transition-fast);
}

.dropdown-menu li a:hover {
  background: rgba(255, 255, 255, 0.1) !important;
  color: var(--accent-orange) !important;
  padding-left: 1.5rem !important;
}

/* Desktop Hover Interaction */
@media (min-width: 769px) {
  .nav-list li.dropdown:hover .dropdown-menu {
    opacity: 1;
    visibility: visible;
    transform: translateX(-50%) translateY(0);
  }
}

/* Mobile Dropdown Interaction */
@media (max-width: 768px) {
  .dropdown-menu {
    position: static;
    transform: none;
    opacity: 1;
    visibility: visible;
    display: none; /* Controlled by JS */
    background: rgba(255, 255, 255, 0.05);
    border: none;
    border-radius: 4px;
    margin-top: 0.25rem;
    box-shadow: none;
    min-width: 100%;
    max-height: none;
  }
  
  .dropdown-menu li a {
    padding: 0.5rem 1.5rem !important;
  }
  
  .dropdown-menu.show {
    display: block;
  }
}
"""
        with open(css_file, "a") as f:
            f.write(dropdown_css)
        print("Updated styles.css with dropdown menu styles.")

# Common Navigation Generator
def get_navigation(active_page=""):
    nav_html = """      <nav class="main-nav" role="navigation" aria-label="Main Navigation">
        <ul class="nav-list">
          <li><a href="index.html" class="{index_active}">Home</a></li>
          <li><a href="categories.html" class="{categories_active}">Categories</a></li>
          <li class="dropdown">
            <a href="#" class="dropdown-toggle" aria-haspopup="true" aria-expanded="false">Popular Schemes <span class="arrow">▼</span></a>
            <ul class="dropdown-menu">
"""
    for s in SCHEMES[:12]: # Top 12 popular schemes in dropdown
        nav_html += f'              <li><a href="{s["id"]}.html">{s["title"]}</a></li>\n'
    
    nav_html += """            </ul>
          </li>
          <li><a href="about.html" class="{about_active}">About</a></li>
          <li><a href="contact.html" class="{contact_active}">Contact</a></li>
        </ul>
      </nav>"""
      
    index_active = "active" if active_page == "index" else ""
    categories_active = "active" if active_page == "categories" else ""
    about_active = "active" if active_page == "about" else ""
    contact_active = "active" if active_page == "contact" else ""
    
    return nav_html.format(
        index_active=index_active,
        categories_active=categories_active,
        about_active=about_active,
        contact_active=contact_active
    )

# Common Footer Generator
def get_footer():
    footer_html = """  <footer class="site-footer" role="contentinfo">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-about">
          <span class="logo-text">🏛️ Yojana<span style="color: var(--accent-orange);">Guide</span></span>
          <p>Your trusted source for comprehensive information about Indian government schemes.</p>
          <div class="social-links">
            <a href="about.html" class="social-link" aria-label="About Us">ℹ️</a>
            <a href="contact.html" class="social-link" aria-label="Contact">✉️</a>
            <a href="categories.html" class="social-link" aria-label="Categories">📂</a>
          </div>
        </div>
        <div>
          <h4 class="footer-heading">Popular Schemes</h4>
          <ul class="footer-links">
"""
    for s in SCHEMES[:6]:
        footer_html += f'            <li><a href="{s["id"]}.html">{s["title"]}</a></li>\n'
        
    footer_html += """          </ul>
        </div>
        <div>
          <h4 class="footer-heading">Categories</h4>
          <ul class="footer-links">
            <li><a href="categories.html">Agriculture</a></li>
            <li><a href="categories.html">Health</a></li>
            <li><a href="categories.html">Housing</a></li>
            <li><a href="categories.html">Education</a></li>
            <li><a href="categories.html">Women &amp; Child</a></li>
            <li><a href="categories.html">Financial Inclusion</a></li>
          </ul>
        </div>
        <div>
          <h4 class="footer-heading">Important Links</h4>
          <ul class="footer-links">
            <li><a href="about.html">About Us</a></li>
            <li><a href="contact.html">Contact Us</a></li>
            <li><a href="privacy-policy.html">Privacy Policy</a></li>
            <li><a href="disclaimer.html">Disclaimer</a></li>
            <li><a href="terms.html">Terms &amp; Conditions</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 Yojana Guide. All rights reserved.</p>
        <p><a href="privacy-policy.html">Privacy</a> · <a href="terms.html">Terms</a> · <a href="disclaimer.html">Disclaimer</a></p>
      </div>
    </div>
  </footer>"""
    return footer_html

# Generate All Scheme Article Pages
def generate_scheme_pages():
    for s in SCHEMES:
        cat_info = CATEGORIES[s["category"]]
        related_schemes = [rs for rs in SCHEMES if rs["category"] == s["category"] and rs["id"] != s["id"]]
        
        # Build Table of Contents dynamically
        toc_html = """            <div class="toc">
              <h4>📑 Table of Contents</h4>
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
            
        # Build Sidebar Related Links
        sidebar_html = f"""        <aside class="sidebar" role="complementary">
          <div class="sidebar-widget">
            <h4>📂 Scheme Category</h4>
            <div class="category-badge">{cat_info["emoji"]} {cat_info["name"]}</div>
          </div>
          <div class="sidebar-widget">
            <h4>🔗 Related Schemes</h4>
            <ul class="related-links">
"""
        for rs in related_schemes[:4]:
            sidebar_html += f'              <li><a href="{rs["id"]}.html">{rs["title"]}</a></li>\n'
        if not related_schemes:
            sidebar_html += '              <li><a href="categories.html">View All Schemes</a></li>\n'
            
        sidebar_html += """            </ul>
          </div>
          <div class="sidebar-widget promo-widget">
            <h4>💡 Need Assistance?</h4>
            <p>For official support, contact your local Gram Panchayat or authorized government helpdesk details provided on official portal.</p>
          </div>
        </aside>"""

        # Build eligibility list HTML
        eligibility_html = "<ul>\n"
        for item in s["eligibility_list"]:
            eligibility_html += f"              <li>{item}</li>\n"
        eligibility_html += "            </ul>\n"
        
        if "exclusions_list" in s and s["exclusions_list"]:
            eligibility_html += "            <h3>Who is Excluded?</h3>\n            <ul>\n"
            for item in s["exclusions_list"]:
                eligibility_html += f"              <li>{item}</li>\n"
            eligibility_html += "            </ul>\n"

        # Build documents list HTML
        documents_html = "<ul>\n"
        for item in s["documents_list"]:
            documents_html += f"              <li>{item}</li>\n"
        documents_html += "            </ul>\n"

        # Build apply steps HTML
        apply_html = "<ol>\n"
        for item in s["apply_steps"]:
            apply_html += f"              <li>{item}</li>\n"
        apply_html += "            </ol>\n"

        # Build status steps HTML
        status_html = "<ol>\n"
        for item in s["status_steps"]:
            status_html += f"              <li>{item}</li>\n"
        status_html += "            </ol>\n"

        # Build FAQ HTML
        faq_html = '<div class="faq-accordion">\n'
        for faq in s["faqs"]:
            faq_html += f"""              <div class="faq-item">
                <h3 class="faq-question">❓ {faq["q"]}</h3>
                <div class="faq-answer">
                  <p>{faq["a"]}</p>
                </div>
              </div>\n"""
        faq_html += "            </div>\n"

        # Assemble Full Page HTML
        page_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="{s["meta_desc"]}">
  <meta name="keywords" content="{s["meta_keywords"]}">
  <meta name="robots" content="index, follow">
  <title>{s["fullname"]} - Eligibility, Benefits | Yojana Guide</title>
  <meta property="og:title" content="{s["fullname"]} - Complete Guide">
  <meta property="og:description" content="{s["meta_desc"]}">
  <meta property="og:type" content="article">
  <link rel="canonical" href="https://www.yojanaguide.in/{s["id"]}.html">
  <link rel="stylesheet" href="styles.css">

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "{s["fullname"]} - Complete Guide",
    "description": "{s["meta_desc"]}",
    "author": {{ "@type": "Organization", "name": "Yojana Guide" }},
    "publisher": {{ "@type": "Organization", "name": "Yojana Guide" }},
    "datePublished": "2026-02-10",
    "dateModified": "2026-07-05",
    "mainEntityOfPage": "https://www.yojanaguide.in/{s["id"]}.html"
  }}
  </script>
</head>
<body>

  <div class="reading-progress" aria-hidden="true"></div>

  <header class="site-header" role="banner">
    <div class="header-inner">
      <a href="index.html" class="site-logo" aria-label="Yojana Guide Home">
        <span class="logo-icon" aria-hidden="true">🏛️</span>
        <span class="logo-text">Yojana<span>Guide</span></span>
      </a>
      {get_navigation()}
      <button class="hamburger" aria-label="Toggle navigation menu" aria-expanded="false"><span></span><span></span><span></span></button>
    </div>
    <div class="nav-overlay" aria-hidden="true"></div>
  </header>

  <nav class="breadcrumb" aria-label="Breadcrumb">
    <div class="container">
      <ol class="breadcrumb-list">
        <li><a href="index.html">Home</a></li>
        <li class="breadcrumb-separator" aria-hidden="true">›</li>
        <li><a href="categories.html">{cat_info["name"]}</a></li>
        <li class="breadcrumb-separator" aria-hidden="true">›</li>
        <li class="current" aria-current="page">{s["title"]}</li>
      </ol>
    </div>
  </nav>

  <main id="main-content" role="main">
    <div class="container">
      <div class="article-layout">

        <!-- Article Content -->
        <article>
          <div class="article-content">
            <div class="article-header">
              <span class="scheme-card-tag {cat_info["class"]}">{cat_info["name"]}</span>
              <h1>{s["fullname"]}</h1>
              <div class="article-meta">
                <span>📅 Updated: July 5, 2026</span>
                <span>⏱️ 9 min read</span>
                <span>{cat_info["emoji"]} {cat_info["name"]}</span>
              </div>
            </div>

            {toc_html}

            <h2 id="overview">Scheme Overview</h2>
            <p>{s["intro"]}</p>

            <h2 id="benefits">Benefits &amp; Financial Assistance</h2>
            <p>{s["benefits_text"]}</p>
            {s["table_html"]}

            <h2 id="eligibility">Eligibility Criteria</h2>
            {eligibility_html}

            <h2 id="documents">Documents Required</h2>
            {documents_html}

            <h2 id="apply">How to Apply</h2>
            {apply_html}

            <h2 id="status">Status Check</h2>
            {status_html}

            <h2 id="faq">Frequently Asked Questions (FAQs)</h2>
            {faq_html}
          </div>
        </article>

        <!-- Sidebar -->
        {sidebar_html}

      </div>
    </div>
  </main>

  {get_footer()}

  <button class="back-to-top" aria-label="Back to top">↑</button>
  <script src="script.js"></script>
</body>
</html>"""

        with open(f"c:\\Users\\durga\\OneDrive\\Desktop\\yojana\\{s['id']}.html", "w", encoding="utf-8") as f:
            f.write(page_html)
            
    print(f"Generated {len(SCHEMES)} scheme pages successfully.")

# Update Existing General Pages with New Header and Footer
def update_general_pages():
    general_files = ["about.html", "contact.html", "privacy-policy.html", "disclaimer.html", "terms.html", "categories.html", "index.html"]
    
    for filename in general_files:
        filepath = f"c:\\Users\\durga\\OneDrive\\Desktop\\yojana\\{filename}"
        if not os.path.exists(filepath):
            continue
            
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
            
        content = "".join(lines)
        
        # 1. Update Navigation Block
        import re
        nav_pattern = r'<nav class="main-nav" role="navigation" aria-label="Main Navigation">.*?</nav>'
        active_key = filename.replace(".html", "")
        content = re.sub(nav_pattern, get_navigation(active_key), content, flags=re.DOTALL)
        
        # 2. Update Footer Block
        footer_pattern = r'<footer class="site-footer" role="contentinfo">.*?</footer>'
        content = re.sub(footer_pattern, get_footer(), content, flags=re.DOTALL)
        
        # 3. If filename is categories.html, rebuild the category list to include all new schemes!
        if filename == "categories.html":
            categories_html_replacement = ""
            for cat_id, cat_info in CATEGORIES.items():
                cat_schemes = [s for s in SCHEMES if s["category"] == cat_id]
                schemes_links_str = " · ".join([f'<a href="{s["id"]}.html">{s["title"]}</a>' for s in cat_schemes])
                
                # Setup custom category description
                desc = ""
                if cat_id == "agriculture":
                    desc = "Government schemes supporting farmers with financial assistance, crop insurance, irrigation subsidies, and agricultural loans."
                elif cat_id == "health":
                    desc = "Healthcare schemes providing insurance coverage, medical assistance, and hospital access for families."
                elif cat_id == "housing":
                    desc = "Affordable housing programs and rooftop solar utility subsidy programs providing direct incentives."
                elif cat_id == "education":
                    desc = "Scholarship programs, skill training initiatives, and educational assistance for students and traditional artisans."
                elif cat_id == "women":
                    desc = "Empowerment programs for women and children including savings schemes, maternity benefits, and nutrition programs."
                elif cat_id == "finance":
                    desc = "Banking access, micro-finance loans, pension schemes, and entrepreneurship support programs."
                elif cat_id == "employment":
                    desc = "Employment guarantees, job creation initiatives, and seed funding support for startups."
                elif cat_id == "pension":
                    desc = "Social security, pensions, and insurance safety nets for unorganized workers and senior citizens."

                categories_html_replacement += f"""
          <div class="category-full-card">
            <span class="cat-icon" aria-hidden="true">{cat_info["emoji"]}</span>
            <h3>{cat_info["name"]}</h3>
            <p>{desc}</p>
            <span class="scheme-count">Schemes: {schemes_links_str}</span>
          </div>"""
            
            grid_pattern = r'<div class="categories-page-grid">.*?</div>\s*</div>'
            replacement_grid = f'<div class="categories-page-grid">{categories_html_replacement}\n        </div>\n      </div>'
            content = re.sub(grid_pattern, replacement_grid, content, flags=re.DOTALL)
            
        # 4. If filename is index.html, update the Featured Schemes cards to link to all active schemes
        if filename == "index.html":
            # Rebuild Featured Schemes section cards
            schemes_cards_html = ""
            for s in SCHEMES[:12]: # Show top 12 on index page
                cat_info = CATEGORIES[s["category"]]
                schemes_cards_html += f"""          <article class="scheme-card">
            <div class="scheme-card-icon {cat_info["color"]}" aria-hidden="true">{s["emoji"]}</div>
            <span class="scheme-card-tag {cat_info["class"]}">{cat_info["name"]}</span>
            <h3><a href="{s["id"]}.html">{s["title"]}</a></h3>
            <p>{s["description"]}</p>
            <a href="{s["id"]}.html" class="card-link">Read Full Guide →</a>
          </article>\n"""
            
            grid_pattern = r'<div class="schemes-grid">.*?</div>'
            replacement_grid = f'<div class="schemes-grid">\n{schemes_cards_html}        </div>'
            content = re.sub(grid_pattern, replacement_grid, content, flags=re.DOTALL)
            
            # Also let's update categories listing on homepage
            cat_list_html = ""
            for cat_id, cat_info in CATEGORIES.items():
                cat_list_html += f"""          <div class="category-card">
            <div class="category-icon" aria-hidden="true">{cat_info["emoji"]}</div>
            <h3>{cat_info["name"]}</h3>
            <p>Browse all active {cat_info["name"]} schemes.</p>
            <a href="categories.html" class="category-link">View Schemes →</a>
          </div>\n"""
            
            cat_grid_pattern = r'<div class="categories-grid">.*?</div>'
            replacement_cat_grid = f'<div class="categories-grid">\n{cat_list_html}        </div>'
            content = re.sub(cat_grid_pattern, replacement_cat_grid, content, flags=re.DOTALL)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
            
    print("Updated general pages with new navigation, footer, categories list, and homepage links.")

# Generate updated sitemap.xml
def generate_sitemap():
    sitemap_file = "c:\\Users\\durga\\OneDrive\\Desktop\\yojana\\sitemap.xml"
    
    general_files = ["index.html", "categories.html", "about.html", "contact.html", "privacy-policy.html", "disclaimer.html", "terms.html"]
    
    sitemap_content = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
"""
    # General files
    for gf in general_files:
        sitemap_content += f"""  <url>
    <loc>https://www.yojanaguide.in/{gf}</loc>
    <lastmod>2026-07-06</lastmod>
    <changefreq>weekly</changefreq>
    <priority>{"1.0" if gf == "index.html" else "0.8"}</priority>
  </url>\n"""
  
    # Schemes
    for s in SCHEMES:
        sitemap_content += f"""  <url>
    <loc>https://www.yojanaguide.in/{s["id"]}.html</loc>
    <lastmod>2026-07-06</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>\n"""
  
    sitemap_content += "</urlset>"
    
    with open(sitemap_file, "w", encoding="utf-8") as f:
        f.write(sitemap_content)
        
    print("Generated sitemap.xml with all 31+ URLs.")

if __name__ == "__main__":
    update_css()
    update_script()
    generate_scheme_pages()
    update_general_pages()
    generate_sitemap()
    print("ALL DONE! Scheme expansion completed successfully.")
