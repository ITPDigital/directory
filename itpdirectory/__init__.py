
COMPANY_STATUS = (
    ('-1', u'Deleted'),
    (1, u'Draft'),
    (2, u'Awaiting Review'),
    (3, u'Entered By Customer'),
    (4, u'Final'),
)

COMPANY_PERSON_RELATION = (
    (1, u'Owner'),
    (2, u'Share Holder'),
    (3, u'Director'),

)




COMPANY_COMPANY_RELATION = (
    (1, u'Branch'),
    (2, u'Distributor'),
    (3, u'Holding Company'),
    (4, u'Joint Venture'),
    (5, u'Partnership'),
    (6, u'Publicly Listed'),
    (7, u'Reseller'),
    (8, u'Subsidiary - Partially Owned'),
    (9, u'Subsidiary - Wholly Owned'),
)


BRAND_COMPANY_RELATION = (
    (1, u'Reseller'),
    (2, u'Distributor'),
    (3, u'Main office'),

)

PERSON_JOB_FUNCTION = ((1, u'Account Manager (Advertising & PR)'),
 (2, u'Account Manager (Other)'),
 (3, u'Accountant'),
 (4, u'Actor / Actress / Entertainer'),
 (5, u'Administrator / Supervisor'),
 (6, u'Advertising Manager'),
 (7, u'Analyst'),
 (8, u'Anchor / Presenter / Master of Ceremonies'),
 (9, u'Architect'),
 (10, u'Area / Regional / Country Manager'),
 (11, u'Armed Forces Employee'),
 (12, u'Assistant Manager'),
 (13, u'Auditor (Finance)'),
 (14, u'Auditor (Non-Finance)'),
 (15, u'Author'),
 (16, u'Banquet Manager'),
 (17, u'Business Development Director'),
 (18, u'Business Development Manager'),
 (19, u'Cabin Crew'),
 (20, u'Cargo Manager / Freight Manager'),
 (21, u'Catering Manager'),
 (22, u'Chairman'),
 (23, u'Chef'),
 (24, u'Chef de Pastry'),
 (25, u'Chief Commercial Officer (CCO)'),
 (26, u'Chief Executive Officer (CEO)'),
 (27, u'Chief Financial Officer (CFO)'),
 (28, u'Chief Information Officer (CIO)'),
 (29, u'Chief Operating Officer (COO)'),
 (30, u'Chief Technology Officer (CTO)'),
 (31, u'Civil Engineer'),
 (32, u'Commercial Director / Manager'),
 (33, u'Communications Manager'),
 (34, u'Computer Operator'),
 (35, u'Construction Manager'),
 (36, u'Consultant (Non IT)'),
 (37, u'Coordinator'),
 (38, u'Copywriter'),
 (39, u'Customer Services / Support'),
 (40, u'Database Manager / Administrator'),
 (41, u'Department / Branch Manager'),
 (42, u'Dietitian / Nutritionist'),
 (43, u'Director'),
 (44, u'Doctor / Physician'),
 (45, u'Document Controller'),
 (46, u'Engineer (Non IT)'),
 (47, u'Events / Conference Manager'),
 (48, u'Executive Assistant / Personal Assistant'),
 (49, u'Executive Chef'),
 (50, u'F & B Manager / Director'),
 (51, u'Facilities Manager'),
 (52, u'Fashion Designer'),
 (53, u'Film Producer / Director'),
 (54, u'Finance Director'),
 (55, u'Finance Manager'),
 (56, u'Financial Advisor'),
 (57, u'Financial Controller'),
 (58, u'Fitness Trainer / Therapist'),
 (59, u'General Manager'),
 (60, u'Government Official'),
 (61, u'Graphic Designer'),
 (62, u'Ground / Airport Staff'),
 (63, u'Guest Services Manager / Concierge / Front Office Manager'),
 (64, u'Head of Department'),
 (65, u'Health & Safety Manager'),
 (66, u'Homemaker'),
 (67, u'Hotel Staff'),
 (68, u'Housekeeping Manager'),
 (69, u'Human Resource Manager'),
 (70, u'Interior Designer'),
 (71, u'IT / Web Developer'),
 (72, u'IT Consultant'),
 (73, u'IT Director'),
 (74, u'IT Engineer'),
 (75, u'IT Manager'),
 (76, u'IT Programmer / Analyst'),
 (77, u'IT Security Manager'),
 (78, u'Journalist / Editor'),
 (79, u'Judge'),
 (80, u'Lawyer'),
 (81, u'Librarian'),
 (82, u'Logistics Manager'),
 (83, u'Maitre De'),
 (84, u'Maketing Director / Chief Marketing Officer'),
 (85, u'Management Trainee'),
 (86, u'Manager'),
 (87, u'Managing Director'),
 (88, u'Marketing Executive'),
 (89, u'Marketing Manager'),
 (90, u'Network Administrator / Manager'),
 (91, u'Operations Manager'),
 (92, u'Owner / Proprietor'),
 (93, u'Partner'),
 (94, u'Pharmacist'),
 (95, u'Pilot'),
 (96, u'Police / Firefighter'),
 (97, u'President'),
 (98, u'Product Manager'),
 (99, u'Professor / Teacher / Instructor'),
 (100, u'Project Manager / Leader (Construction)'),
 (101, u'Project Manager / Leader (IT)'),
 (102, u'Project Manager / Leader (Other)'),
 (103, u'Public Relations Executive'),
 (104, u'Public Relations Manager'),
 (105, u'Purchase Manager / Buyer'),
 (106, u'Quantity Surveyor'),
 (107, u'Real Estate Agent / Broker'),
 (108, u'Recruitment Manager'),
 (109, u'Relationship Manager (Banking)'),
 (110, u'Resident Manager'),
 (111, u'Restaurant Manager'),
 (112, u'Retired'),
 (113, u'Safety Engineer'),
 (114, u'Sales Director'),
 (115, u'Sales Engineer'),
 (116, u'Sales Executive'),
 (117, u'Sales Manager'),
 (118, u'Scientist / Researcher'),
 (119, u'Secretary / Office Staff / Clerical Staff '),
 (120, u'Senior Executive'),
 (121, u'Senior Manager'),
 (122, u'Software Engineer'),
 (123, u'Sous Chef'),
 (124, u'Stock Broker'),
 (125, u'Store Manager'),
 (126, u'Student'),
 (127, u'Support Manager / Executive'),
 (128, u'Systems Analyst'),
 (129, u'Technician'),
 (130, u'Trainee'),
 (131, u'Training Manager'),
 (132, u'Travel Consultant / Agent'),
 (133, u'Unemployed'),
 (134, u'Vice President / Senior Vice President'),
 (135, u'Videographer / Photographer'),
 (136, u'Web / Online Designer'))


MAIN_INDUSTRY = (

     (0, u'N/A'),
     (1, u'Agriculture'),
     (2, u'Art & Design'),
     (3, u'Automotive'),
     (4, u'Aviation'),
     (5, u'Banking'),
     (6, u'Broadcast'),
     (7, u'Cargo / Freight'),
     (8, u'Communications'),
     (9, u'Construction'),
     (10, u'Education Services'),
     (11, u'Electronics / Electrical'),
     (12, u'Energy & Power'),
     (13, u'Entertainment'),
     (14, u'Finance & Insurance'),
     (15, u'FMCG / Retail'),
     (16, u'Government'),
     (17, u'Healthcare'),
     (18, u'Hospitality'),
     (19, u'IT'),
     (20, u'Law'),
     (21, u'Marketing / Publishing'),
     (22, u'Mining'),
     (23, u'Oil & Gas'),
     (24, u'Other'),
     (25, u'Real Estate'),
     (26, u'Recruitment'),
     (27, u'Service and Maintenance'),
     (28, u'Shipping & Marine'),
     (29, u'Textile'),
     (30, u'Transportation'),
     (31, u'Travel and Tourism'),
     (32, u'Wholesale Trade'),
)

SPECIFIC_INDUSTRY = ( 
 (0, u'N/A'),
 (1, u'Consultant (Agriculture)'),
 (2, u'Epiculture'),
 (3, u'Farming'),
 (4, u'Farming Equipment Distributor / Reseller'),
 (5, u'Farming Equipment Manufacturer'),
 (6, u'Fertilizer / Agriculture Chemicals Distributor / Reseller'),
 (7, u'Fertilizer / Agriculture Chemicals Manufacturer'),
 (8, u'Field Crops / Soil Management'),
 (9, u'Fishing and Fish Processing'),
 (10, u'Floriculture / Horticulture'),
 (11, u'Irrigation'),
 (12, u'Meats / Provisions'),
 (13, u'Misc. Agricultural Services'),
 (14, u'Produce Fruits / Vegetables'),
 (15, u'Produce Sugar / Tea / Coffee / Spices / Tobacco'),
 (16, u'Seed / Nursery Trade'),
 (17, u'Antique & Handicraft'),
 (18, u'Graphic Design'),
 (19, u'Image / Picture Gallery'),
 (20, u'Interior Designers / Decorators'),
 (21, u'Photo Studio'),
 (22, u'Picture Frames & Art Gallery'),
 (23, u'Auto Dealers'),
 (24, u'Auto Parts and Accessories Manufacturer'),
 (25, u'Auto Parts and Accessories Supplier'),
 (26, u'Automotive Manufacturers'),
 (27, u'Automotive Repairing & Servicing'),
 (28, u'Air Cargo / Freight'),
 (29, u'Air Ticket Booking Services'),
 (30, u'Aircraft Engine Manufacturer'),
 (31, u'Aircraft Manufacturer'),
 (32, u'Airline (Passenger)'),
 (33, u'Airport / Airport Free Zone'),
 (34, u'Airport Operations, Services & Maintenance'),
 (35, u'Airport Supplier (non IT)'),
 (36, u'Aviation IT Systems'),
 (37, u'Aviation MRO'),
 (38, u'Aviation Training & Education'),
 (39, u'Business Aviation Services / Air Craft Charter'),
 (40, u'Civil Aviation Ministry'),
 (41, u'Components & Avionics Distributor / Reseller'),
 (42, u'Components & Avionics Manufacturer'),
 (43, u'Consultant (Aviation)'),
 (44, u'Duty Free Operators'),
 (45, u'Ground Handling'),
 (46, u'Central Bank'),
 (47, u'Commercial Bank'),
 (48, u'Consultant (Banking)'),
 (49, u'Investment and Merchant Bank'),
 (50, u'Specialized Bank'),
 (51, u'Audio / Video Equipment Distributor'),
 (52, u'Audio / Video Equipment Reseller'),
 (53, u'Audio / Visual Equipment Manufacturer'),
 (54, u'Broadcast Software'),
 (55, u'Censor Bureaus'),
 (56, u'Consultant (Broadcast)'),
 (57, u'Film & Cinema Training'),
 (58, u'Film Distributors'),
 (59, u'Film Producers / Financers / Promoters'),
 (60, u'Film, Cinema & Recording Studios'),
 (61, u'Post Production Houses'),
 (62, u'Production Houses'),
 (63, u'Radio Broadcaster'),
 (64, u'Satellite Equipment Distributor / Reseller'),
 (65, u'Satellite Equipment Manufacturer'),
 (66, u'Special Effects / CGI / Multimedia'),
 (67, u'Television Broadcaster'),
 (68, u'Air Freight'),
 (69, u'Cargo / Freight Forwarders'),
 (70, u'Clearing & Forwarding'),
 (71, u'Logistics'),
 (72, u'Moving Companies'),
 (73, u'Comms Equipment Distributor'),
 (74, u'Comms Equipment Maintenance'),
 (75, u'Comms Equipment Reseller'),
 (76, u'Communication Softwares Manufacturer'),
 (77, u'Communications Equipment Manufacturer'),
 (78, u'ISP'),
 (79, u'MTC / PTT Telecommunications Ministry'),
 (80, u'Telecommunications Service Provider'),
 (81, u'Aluminium Cladding / Roofing Manufacturer / Supplier'),
 (82, u'Architect'),
 (83, u'Architectural Hardware'),
 (84, u'Auction Houses / Tenders'),
 (85, u'Automated Door Systems Manufacturer'),
 (86, u'Bathroom Accessories and fixtures Manufacturer / Supplier'),
 (87, u'Blasting Equipment Manufacturer'),
 (88, u'Blasting Equipment Supplier'),
 (89, u'Building Energy Management Systems'),
 (90, u'Building Materials Manufacturer'),
 (91, u'Building Materials Supplier'),
 (92, u'Cable Laying Contractors'),
 (93, u'Cable Manufacturer / Supplier'),
 (94, u'Car Parking Systems'),
 (95, u'Civil Engineering Contractors'),
 (96, u'Construction - Consultant'),
 (97, u'Construction - Contractor'),
 (98, u'Construction Chemicals Manufacturer / Supplier'),
 (99, u'Construction Equipment Distributor / Reseller'),
 (100, u'Construction Equipment Manufacturer'),
 (101, u'Construction Labour Supply Services'),
 (102, u'Construction Machinery Maintenance'),
 (103, u'Construction Machinery Manufacturer / Distributor'),
 (104, u'Consultancy Services'),
 (105, u'Contractors - FM'),
 (106, u'Contractors - General'),
 (107, u'Contractors - MEP'),
 (108, u'Crane Manufacturer / Supplier'),
 (109, u'De-Salination'),
 (110, u'Drainage & Pipes Equipment Manufacturer / Supplier'),
 (111, u'Dredging and Excavation'),
 (112, u'Ducting & Insulation'),
 (113, u'Elevators & Escalators Manufacturer / Supplier'),
 (114, u'Engineering Machinery Manufacturer / Supplier'),
 (115, u'Fencing & Site Hoardings'),
 (116, u'Fibre Glass Manufacturer / Supplier'),
 (117, u'Flooring & Tiles Manufacturer / Retailer'),
 (118, u'Formwork / Scaffolding'),
 (119, u'Foundation & Piling'),
 (120, u'Furniture Indoor - Manufacturer / Retailer'),
 (121, u'Furniture Manufacturer / Retailer'),
 (122, u'Furniture Office - Manufacturer / Retailer'),
 (123, u'Furniture Outdoor - Manufacturer / Retailer'),
 (124, u'General Maintenance (Construction)'),
 (125, u'Glass Manufacturer / Supplier'),
 (126, u'Health & Safety Services / Equipment'),
 (127, u'Hoists Manufacturer / Supplier'),
 (128, u'HVAC Equipment Maintenance'),
 (129, u'HVAC Equipment Manufacturer'),
 (130, u'HVAC Equipment Supplier'),
 (131, u'Kitchens Commercial - Manufacturer / Supplier'),
 (132, u'Kitchens Residential - Manufacturer / Supplier'),
 (133, u'Landscape Designers'),
 (134, u'Landscaping'),
 (135, u'Lighting Indoor Manufacturer / Supplier'),
 (136, u'Lighting Manufacturer / Supplier'),
 (137, u'Lighting Outdoor Manufacturer / Supplier'),
 (138, u'Misc. Construction Services'),
 (139, u'Paint Manufacturer / Supplier'),
 (140, u'Plant Rental Services'),
 (141, u'Power Tools Manufacturer / Supplier'),
 (142, u'Pre-cast Concrete'),
 (143, u'Pre-Fabricated Buildings'),
 (144, u'Project Management and Engineering'),
 (145, u'Pumps & Valves Manufacturer / Supplier'),
 (146, u'Quality Control / Material Testing Services'),
 (147, u'Quantity / Quality Surveyors'),
 (148, u'Quarrying'),
 (149, u'Readymix Cement Suppliers'),
 (150, u'Security Equipment / Products'),
 (151, u'Steel Manufacturer / Supplier'),
 (152, u'Stone / Aggregate Supplier'),
 (153, u'Surveying Equipment Manufacturer / Supplier'),
 (154, u'Tools Manufacturer / Supplier'),
 (155, u'WallCovering Manufacturer / Retailer'),
 (156, u'Water Proofing'),
 (157, u'College'),
 (158, u'Driving Institutes'),
 (159, u'Educational Institutes'),
 (160, u'Research Institute'),
 (161, u'Schools'),
 (162, u'Training Institutes'),
 (163, u'University'),
 (164, u'Consumer Electronics Manufacturer'),
 (165, u'Consumer Electronics Trading'),
 (166, u'Electric Equipment Manufacturer'),
 (167, u'Electric Equipment Supplier'),
 (168, u'Electronic Components and Accessories Manufacturer'),
 (169, u'Electronic Components and Accessories Supplier'),
 (170, u'Home Appliances Manufacturer'),
 (171, u'Home Appliances Trading'),
 (172, u'Security & Surveillance Systems'),
 (173, u'Watch Manufacturer'),
 (174, u'Watch Store / Supplier'),
 (175, u'Water Pumps'),
 (176, u'Downstream Services'),
 (177, u'Electric / Gas Utility'),
 (178, u'Electric Power Generation and Transmission'),
 (179, u'Electric Utility'),
 (180, u'Energy Conversion and Storage'),
 (181, u'Energy Service Company'),
 (182, u'Energy Service Provider'),
 (183, u'Federal Power'),
 (184, u'Fusion Energy'),
 (185, u'Generator / Temp. Power Supply Manufacturer / Supplier'),
 (186,
  u'Hydrogen, Natural (Solid / Liquid / Gaseous Refuse-Derived Fuels / Wood) & Synthetic Fuels'),
 (187, u'Municipality'),
 (188, u'Nuclear Energy (Fuels, Power Plant, Technology)'),
 (189, u'Renewable Energies (Solar, Wind, Geothermal, etc.)'),
 (190, u'Solar Power Manufacturer / Supplier'),
 (191, u'Testing & Monitoring'),
 (192, u'Water Desalination'),
 (193, u'Water Utility / System'),
 (194, u'Cinemas & Theatres'),
 (195, u'Entertainment Services'),
 (196, u'Event / Exhibition Organizers'),
 (197, u'Film and Music'),
 (198, u'Auditors'),
 (199, u'Consultant (Finance & Insurance)'),
 (200, u'Credit and Finance Company'),
 (201, u'Credit Guarantee Organizations'),
 (202, u'Credit Rating and Debt Collection'),
 (203, u'Development and Aid Institutions'),
 (204, u'Financial Institutions'),
 (205, u'Financial Services (Misc.)'),
 (206, u'Foreign Exchange Dealers'),
 (207, u'Insurance Agents'),
 (208, u'Insurance Companies'),
 (209, u'Insurance Solutions & Financial Services'),
 (210, u'Investment Companies'),
 (211, u'Investment Promotion Authorities'),
 (212, u'Money Transfer and Exchange Dealers'),
 (213, u'Mutual and Stock Funds'),
 (214, u'Offshore Banking Units'),
 (215, u'Regulatory and Administrative Bodies'),
 (216, u'Securities Markets'),
 (217, u'Stock Brokers / Traders'),
 (218, u'Stock Exchange'),
 (219, u'Abrasives and Adhesive Products'),
 (220, u'Bakeries and Confectioneries'),
 (221, u'Boutiques'),
 (222, u'Cold Stores'),
 (223, u'Cosmetics / Fashion Products Manufacturer'),
 (224, u'Cosmetics / Fashion Products Trading'),
 (225, u'Department and Variety Stores'),
 (226, u'Edible Oil and Oil Products Manufacturer'),
 (227, u'Edible Oil and Oil Products Trading'),
 (228, u'Eyewear Products Manufacturer'),
 (229, u'Eyewear Products Trading'),
 (230, u'FMCG Distributor'),
 (231, u'FMCG Manufacturer'),
 (232, u'FMCG Retailer'),
 (233, u'Food & Dairy Products Manufacturer'),
 (234, u'Food & Dairy Products Trading'),
 (235, u'Food and Beverages Distributor'),
 (236, u'Food and Beverages Manufacturer'),
 (237, u'Food Processing / Distribution'),
 (238, u'Glass and Crystal Products Trading'),
 (239, u'Hardware and Tools Trading'),
 (240, u'Home Accessories & Gifts'),
 (241, u'Household Chemicals Manufacturer'),
 (242, u'Household Chemicals Trading'),
 (243, u'Household, Glassware, Ceramics Trading'),
 (244, u'Jewellery Manufacturer'),
 (245, u'Jewellery Store / Trader'),
 (246, u'Leather Products and Footwear Manufacturer'),
 (247, u'Leather Products and Footwear Trading'),
 (248, u'Meat / Poultry / Fish Trading'),
 (249, u'Office Equipment Trading'),
 (250, u'Paper & Plastic Products Manufacturer'),
 (251, u'Paper & Plastic Products Trading'),
 (252, u'Pens / Stationery Products Manufacturer'),
 (253, u'Pens / Stationery Products Trading'),
 (254, u'Perfumes Manufacturer'),
 (255, u'Perfumes Trading'),
 (256, u'Photographic Equipment Manufacturer'),
 (257, u'Photographic Equipment Trading'),
 (258, u'Shopping Centres and Malls'),
 (259, u'Supermarkets and Departmental Stores'),
 (260, u'Tobacco & Cigarettes Manufacturer'),
 (261, u'Tobacco & Cigarettes Trading'),
 (262, u'Toiletries and Personal Care Products'),
 (263, u'Toys and Sporting Goods Manufacturer'),
 (264, u'Toys and Sporting Goods Trading'),
 (265, u'Tyres and Rubber Products Manufacturer'),
 (266, u'Tyres and Rubber Products Trading'),
 (267, u'Ambulance Services'),
 (268, u'Army / Airforce / Navy / Defense Ministry'),
 (269, u'Embassies & Consulates'),
 (270, u'Fire Services'),
 (271, u'Government (Federal)'),
 (272, u'Government (Local)'),
 (273, u'Other Government Ministry / Public Utility'),
 (274, u'Police Services'),
 (275, u'Ambulatory Services'),
 (276, u'Ayurvedic Therapies'),
 (277, u'Biotechnological Sciences'),
 (278, u'Clinic'),
 (279, u'Consultant - Medical Solutions'),
 (280, u'Cosmetic Surgery'),
 (281, u'Dental Association'),
 (282, u'Dental Clinic'),
 (283, u'Dental Laboratory'),
 (284, u'Dental Manufacturer'),
 (285, u'Dental School'),
 (286, u'Dental Supplier'),
 (287, u'Drugs / Pharmaceuticals / Chemicals Manufacturer'),
 (288, u'Drugs / Pharmaceuticals / Chemicals Trading'),
 (289, u'Health and Beauty Aid'),
 (290, u'Health Club & Gymnasiums'),
 (291, u'Healthcare (Misc.)'),
 (292, u'Healthcare Publication'),
 (293, u'Hospital'),
 (294, u'Imaging'),
 (295, u'Laboratory'),
 (296, u'Medical and Scientific Equipment and Supplies'),
 (297, u'Medical and Scientific Equipment Products Manufacturer'),
 (298, u'Medical Logistics'),
 (299, u'Ministry of Health'),
 (300, u'Pharmacy'),
 (301, u'Physiotherapy'),
 (302, u'Science / Research & Development'),
 (303, u'Training Services'),
 (304, u'Veterinary Clinic'),
 (305, u'Banquet Services'),
 (306, u'Catering'),
 (307, u'Flight Catering'),
 (308, u'Hospitality Consultancy'),
 (309, u'Hotel Supplies'),
 (310, u'Hotels / Resorts'),
 (311, u'Laundry Services'),
 (312, u'Leisure & Spa'),
 (313, u'Restaurants / Bars / Fastfood'),
 (314, u'Computer Distributor'),
 (315, u'Computer Hardware Manufacturer'),
 (316, u'Computer Maintenance'),
 (317, u'Computer Reseller'),
 (318, u'Computer Software Manufacturer / Developer'),
 (319, u'Computer Training'),
 (320, u'Internet / Web Related'),
 (321, u'IT Consultant'),
 (322, u'System Integrator'),
 (323, u'Value Added Reseller'),
 (324, u'Advocate'),
 (325, u'Lawyers & Legal Consultants'),
 (326, u'Legal Services'),
 (327, u'Advertising Agency'),
 (328, u'Advertising Representatives'),
 (329, u'Bookshops and Newsagents'),
 (330, u'Circulation Auditors'),
 (331, u'Direct Marketing'),
 (332, u'Distribution'),
 (333, u'Journalist Associations'),
 (334, u'Market Research Services'),
 (335, u'Media Buying Agencies'),
 (336, u'Media Trade Groups'),
 (337, u'New Media Agencies'),
 (338, u'News Agencies'),
 (339, u'PR Agency'),
 (340, u'Printing Industry'),
 (341, u'Publishing / Journalism'),
 (342, u'Sign Manufacturers & Outdoor Media'),
 (343, u'Metal Mining'),
 (344, u'Mining'),
 (345, u'Mining Services (Misc.)'),
 (346, u'Nonmetallic Minerals'),
 (347, u'Consultants (Oil & Gas)'),
 (348, u'Distribution and Marketing'),
 (349, u'Drilling & Exploration'),
 (350, u'Environmental'),
 (351, u'Fire Safety'),
 (352, u'Gas Distribution and Transmission'),
 (353, u'Geological / Geophysical'),
 (354, u'Integrated Oil Companies'),
 (355, u'Maintenance & Repair (Oil & Gas)'),
 (356, u'Offshore Oil and Gas'),
 (357, u'Oil & Lubricants Equipments'),
 (358, u'Oil / Gas Producer'),
 (359, u'Oil / Lubricants / Greases'),
 (360, u'Oil Transportation'),
 (361, u'Oilfield Services and Equipment'),
 (362, u'Onshore Oil and Gas'),
 (363, u'Petrochemicals and Refining'),
 (364, u'Petroleum Products'),
 (365, u'Pigs Manufacturer / Retailer'),
 (366, u'Pipelines and Shipping'),
 (367, u'Pumps'),
 (368, u'Safety & Security Services O&G'),
 (369, u'Suppliers to Oil & Gas Industry'),
 (370, u'Cable Manufacturers / Suppliers'),
 (371, u'Charity Organisations'),
 (372, u'Consultancy - Misc.'),
 (373, u'Contact Centers'),
 (374, u'Distributor / Supplier Misc.'),
 (375, u'Management Consultant'),
 (376, u'Manufacturing / Processing Misc.'),
 (377, u'Metal / Steel Manufacturer'),
 (378, u'Other'),
 (379, u'Packaging and Printing'),
 (380, u'Sports Associations / Authorities'),
 (381, u'Developers'),
 (382, u'Real Estate & Property Development'),
 (383, u'Real Estate Agents'),
 (384, u'Recruitment Agency'),
 (385, u'Cleaning & Maintenance Services'),
 (386, u'Facilities Management'),
 (387, u'Fire Equipment Manufacturer / Retailer'),
 (388, u'Operation and Maintenance'),
 (389, u'Pest Control'),
 (390, u'Repairing and Servicing'),
 (391, u'Security Services'),
 (392, u'Barges Manufactuer / Maintenance'),
 (393, u'Boat Equipment Manufacturer / Maintenance'),
 (394, u'Global Positioning & Tracking'),
 (395, u'Luxury Vessels'),
 (396, u'Marine Equipment Manufacturer / Maintenance'),
 (397, u'Merchant Vessels'),
 (398, u'Ocean Freight'),
 (399, u'Oil Tankers'),
 (400, u'Safety & Security Services (Shipping)'),
 (401, u'Ship Chandlers'),
 (402, u'Soft Furnishing / Textiles Manufacturer / Supplier'),
 (403, u'Textile Machinery & Equipment'),
 (404, u'Textiles and Apparel Manufacturer'),
 (405, u'Textiles and Apparel Trading'),
 (406, u'Bus Rental'),
 (407, u'Limousine Service'),
 (408, u'Logistics Free Zones'),
 (409, u'Logistics Machinery / Forklift Trucks'),
 (410, u'Packaging & Label Making'),
 (411, u'Ports / Port Operators'),
 (412, u'Public Transport'),
 (413, u'Railway'),
 (414, u'Rent-a-Car'),
 (415, u'Spare Parts'),
 (416, u'Transportation Consultancy'),
 (417, u'Warehouse Management Systems'),
 (418, u'Immigration Consultant'),
 (419, u'Tour Operators'),
 (420, u'Tours and Travel Agencies'),
 (421, u'Travel and Tourism'),
 (422, u'General Trading')
)


INDUSTRY_MAIN_SPECIFIC_MAP =  { 0:[0], 1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], 2: [17, 18, 19, 20, 21, 22], 3: [23, 24, 25, 26, 27], 4: [28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45], 5: [46, 47, 48, 49, 50], 6: [51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67], 7: [68, 69, 70, 71, 72], 8: [73, 74, 75, 76, 77, 78, 79, 80], 9: [81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156], 10: [157, 158, 159, 160, 161, 162, 163], 11: [164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175], 12: [176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193], 13: [194, 195, 196, 197], 14: [198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218], 15: [219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266], 16: [267, 268, 269, 270, 271, 272, 273, 274], 17: [275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304], 18: [305, 306, 307, 308, 309, 310, 311, 312, 313], 19: [314, 315, 316, 317, 318, 319, 320, 321, 322, 323], 20: [324, 325, 326], 21: [327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342], 22: [343, 344, 345, 346], 23: [347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369], 24: [370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380], 25: [381, 382, 383], 26: [384], 27: [385, 386, 387, 388, 389, 390, 391], 28: [392, 393, 394, 395, 396, 397, 398, 399, 400, 401], 29: [402, 403, 404, 405], 30: [406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417], 31: [418, 419, 420, 421], 32: [422]}

