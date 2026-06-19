TEST_CASES = [
    {
        "query": "Does the cotton kurta need dry cleaning?",
        "expected_answer": "No, the cotton kurta is machine washable.",
        "relevant_chunk_ids": ["p001_care", "p001_identity"],
    },
    {
        "query": "What colours does the silk saree come in?",
        "expected_answer": "The silk saree is available in red, gold, and emerald.",
        "relevant_chunk_ids": ["p003_variants"],
    },
    {
        "query": "Is the linen co-ord set suitable for summer?",
        "expected_answer": "Yes, the linen co-ord set is designed for summer casual wear.",
        "relevant_chunk_ids": ["p004_identity"],
    },
    {
        "query": "What is the price of the woolen shawl?",
        "expected_answer": "The woolen shawl is priced at ₹2,199.",
        "relevant_chunk_ids": ["p002_variants"],
    },
    {
        "query": "Can I wear the anarkali suit to a wedding?",
        "expected_answer": "Yes, the anarkali suit is festive wear suitable for weddings and celebrations.",
        "relevant_chunk_ids": ["p005_identity"],
    },
    {
        "query": "Which products are available in size XS?",
        "expected_answer": "The linen co-ord set is available from size XS to XL.",
        "relevant_chunk_ids": ["p004_variants"],
    },
    {
        "query": "How do I care for the woolen shawl?",
        "expected_answer": "The woolen shawl requires dry cleaning only.",
        "relevant_chunk_ids": ["p002_care"],
    },
    {
        "query": "What is the most affordable product in the catalog?",
        "expected_answer": "The cotton kurta is the most affordable at ₹1,299.",
        "relevant_chunk_ids": ["p001_variants"],
    },
    {
        "query": "Is there anything suitable for a festive occasion?",
        "expected_answer": "Yes, the silk saree and the anarkali suit are both festive wear.",
        "relevant_chunk_ids": ["p003_identity", "p005_identity"],
    },
    {
        "query": "Do you have winter clothing?",
        "expected_answer": "Yes, the woolen shawl is designed for winter evenings.",
        "relevant_chunk_ids": ["p002_identity"],
    },
    {
        "query": "What sizes does the anarkali suit come in?",
        "expected_answer": "The anarkali suit is available in sizes S to XXL.",
        "relevant_chunk_ids": ["p005_variants"],
    },
    {
        "query": "Is the silk saree suitable for Diwali?",
        "expected_answer": "Yes, the silk saree is festive wear ideal for Diwali celebrations.",
        "relevant_chunk_ids": ["p003_identity"],
    },
    {
        "query": "Which products can be machine washed?",
        "expected_answer": "The cotton kurta is machine washable.",
        "relevant_chunk_ids": ["p001_care"],
    },
    {
        "query": "Do you have anything in teal?",
        "expected_answer": "Yes, the anarkali suit is available in teal.",
        "relevant_chunk_ids": ["p005_variants"],
    },
    {
        "query": "What is the price of the silk saree?",
        "expected_answer": "The silk saree is priced at ₹4,299.",
        "relevant_chunk_ids": ["p003_variants"],
    },
    {
        "query": "Is there anything for casual daily wear?",
        "expected_answer": "Yes, the cotton kurta and the linen co-ord set are both suited for casual daily wear.",
        "relevant_chunk_ids": ["p001_identity", "p004_identity"],
    },
    {
        "query": "Does the linen co-ord set come in beige?",
        "expected_answer": "Yes, the linen co-ord set is available in beige.",
        "relevant_chunk_ids": ["p004_variants"],
    },
    {
        "query": "What is the most expensive product?",
        "expected_answer": "The silk saree is the most expensive product at ₹4,299.",
        "relevant_chunk_ids": ["p003_variants"],
    },
    {
        "query": "Can I get the woolen shawl in black?",
        "expected_answer": "The woolen shawl is available in charcoal grey and maroon, not black.",
        "relevant_chunk_ids": ["p002_variants"],
    },
    {
        "query": "Do you have anything for a winter wedding?",
        "expected_answer": "I don't have a product that matches that specifically.",
        "relevant_chunk_ids": [],
    },
]