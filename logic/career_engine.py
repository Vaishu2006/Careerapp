def career_after_10th(selections):

    if not selections:
        return ["Please select subject and interest"]

    s = selections.lower().replace(" ", "")

    mapping = {
        ("science", "medical"): "BiPC (Medical Sciences)",
        ("maths", "technology"): "MPC (Engineering/IT)",
        ("maths", "business"): "MEC (Finance & Business)",
        ("maths", "design"): "MPC (Design & Architecture)",
        ("maths", "law"): "MEC (Law path)",

        ("commerce", "business"): "MEC (Commerce & Finance)",
        ("commerce", "technology"): "MEC + IT",
        ("commerce", "law"): "CEC (Law & Civics)",
        ("commerce", "media"): "MEC + Media",

        ("arts", "design"): "Arts & Humanities (Design)",
        ("arts", "media"): "Arts & Journalism",
        ("arts", "law"): "CEC (Law path)",
        ("arts", "business"): "MEC (Management)"
    }

    for (subject, interest), stream in mapping.items():
        if subject in s and interest in s:
            return [stream]

    return ["The pair you selected is a mismatched stream"]
def career_after_12th(stream):

    s = stream.lower()

    degree_map = {
        "mpc": [
            "BTech / Engineering",
            "BSc (Maths / Physics / CS)",
            "Architecture",
            "Defence Services",
            "Aviation"
        ],

        "bipc": [
            "MBBS",
            "BDS (Dental)",
            "BPharmacy",
            "Biotechnology",
            "Nursing",
            "Physiotherapy"
        ],

        "mec": [
            "BCom",
            "CA",
            "BBA",
            "Economics",
            "Banking & Finance"
        ],

        "cec": [
            "Law",
            "Public Administration",
            "BBA",
            "Government Services"
        ],

        "arts": [
            "BA",
            "Design Courses",
            "Journalism",
            "Psychology",
            "Law",
            "Social Sciences"
        ]
    }

    return degree_map.get(s, ["Career guidance recommended"])
def career_after_engineering(branch, interest):

    b = branch.lower()
    i = interest.lower()

    mapping = {

        ("cse", "ai"): [
            "AI Engineer",
            "Machine Learning Engineer",
            "Data Scientist"
        ],

        ("cse", "cloud"): [
            "Cloud Engineer",
            "DevOps Engineer",
            "Site Reliability Engineer"
        ],

        ("cse", "security"): [
            "Cybersecurity Engineer",
            "Security Analyst",
            "Ethical Hacker"
        ],

        ("ece", "core"): [
            "Embedded Systems Engineer",
            "VLSI Engineer",
            "IoT Engineer"
        ],

        ("mech", "core"): [
            "Design Engineer",
            "Automobile Engineer",
            "Manufacturing Engineer"
        ],

        ("civil", "core"): [
            "Structural Engineer",
            "Site Engineer",
            "Urban Planner"
        ],

        ("eee", "core"): [
            "Power Systems Engineer",
            "Electrical Design Engineer",
            "Automation Engineer"
        ],

        ("any", "management"): [
            "Product Manager",
            "Project Manager",
            "Business Analyst"
        ]
    }

    # exact match
    if (b, i) in mapping:
        return mapping[(b, i)]

    # fallback for management
    if i == "management":
        return mapping[("any", "management")]

    return ["Career guidance recommended"]
def medical_specialization(interest):

    i = interest.lower()

    mapping = {
        "surgery": ["MS General Surgery (3 years)"],
        "children": ["MD Pediatrics (3 years)"],
        "skin": ["MD Dermatology (3 years)"],
        "heart": ["DM Cardiology (6 years)"],
        "brain": ["DM Neurology (6 years)"],
        "women": ["MD Gynecology (3 years)"],
        "bones": ["MS Orthopedics (3 years)"],
        "general": ["MD Internal Medicine (3 years)"]
    }

    return mapping.get(i, ["Medical counseling recommended"])
def govt_careers(interest):

    i = interest.lower()

    mapping = {

        "leadership": [
            "UPSC Civil Services (IAS, IPS, IFS)",
            "State Public Service Commission (Group 1, 2)",
            "Indian Forest Service"
        ],

        "finance": [
            "RBI Grade B",
            "SBI PO",
            "IBPS PO",
            "NABARD Officer"
        ],

        "defence": [
            "NDA",
            "CDS",
            "AFCAT",
            "CAPF Assistant Commandant"
        ],

        "clerical": [
            "SSC CGL",
            "SSC CHSL",
            "State Government Clerical Exams"
        ],

        "technical": [
            "RRB (Railways)",
            "ISRO Technical Assistant",
            "PSU Exams (BHEL, NTPC, ONGC)"
        ]
    }

    return mapping.get(i, ["Explore multiple government opportunities"])
def get_roadmap(career):

    career = career.lower()

    roadmaps = {
        "ai engineer": [
            "Learn Python",
            "Maths for AI (Linear Algebra, Probability)",
            "Machine Learning basics",
            "Deep Learning",
            "Projects + Internships",
            "Apply for AI roles"
        ],

        "machine learning engineer": [
            "Python + Data handling",
            "Statistics",
            "ML Algorithms",
            "Model deployment",
            "Real-world projects",
            "Job preparation"
        ],

        "data scientist": [
            "Python & SQL",
            "Statistics",
            "Data visualization",
            "Machine learning",
            "Case studies",
            "Industry projects"
        ],

        "cloud engineer": [
            "Networking basics",
            "Linux",
            "AWS/Azure/GCP",
            "DevOps tools",
            "Cloud projects",
            "Certifications"
        ]
    }

    return roadmaps.get(career, ["Roadmap coming soon for this career"])
