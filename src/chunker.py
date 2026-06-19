def product_to_chunks(product: dict) -> list[dict]:
    pid = product["id"]
    name = product["name"]

    chunks = []

    # Chunk 1 — Identity
    identity_text = (
        f"{name}. {product['description']} "
        f"Category: {product['category']}. "
        f"Fabric: {product.get('fabric', 'not specified')}. "
        f"Occasion: {product.get('occasion', 'general')}."
    )

    chunks.append({
        "id": f"{pid}_identity",
        "text": identity_text,
        "metadata": {
            "product_id": pid,
            "chunk_type": "identity",
            "category": product["category"],
            "price": product.get("price", 0),
        },
    })

    # Chunk 2 — Variants
    variant_text = (
        f"{name} is available in colours: "
        f"{', '.join(product.get('colors', []))}. "
        f"Available sizes: "
        f"{', '.join(product.get('sizes', ['one size']))}. "
        f"Price: ₹{product.get('price', 'not listed')}. "
        f"Stock status: {product.get('stock_status', 'in stock')}."
    )

    chunks.append({
        "id": f"{pid}_variants",
        "text": variant_text,
        "metadata": {
            "product_id": pid,
            "chunk_type": "variants",
            "category": product["category"],
            "price": product.get("price", 0),
        },
    })

    # Chunk 3 — Policy
    if product.get("return_policy"):
        policy_text = (
            f"Return and exchange policy for {name}: "
            f"{product['return_policy']} "
            f"Exchange policy: "
            f"{product.get('exchange_policy', 'contact support for exchanges')}."
        )

        chunks.append({
            "id": f"{pid}_policy",
            "text": policy_text,
            "metadata": {
                "product_id": pid,
                "chunk_type": "policy",
                "category": product["category"],
                "price": product.get("price", 0),
            },
        })

    # Chunk 4 — Care Instructions
    if product.get("care_instructions"):
        care_text = (
            f"Care instructions for {name}: "
            f"{product['care_instructions']}"
        )

        chunks.append({
            "id": f"{pid}_care",
            "text": care_text,
            "metadata": {
                "product_id": pid,
                "chunk_type": "care",
                "category": product["category"],
                "price": product.get("price", 0),
            },
        })

    # Chunk 5+ — FAQs
    for i, faq in enumerate(product.get("faqs", [])):
        faq_text = (
            f"Question about {name}: {faq['question']} "
            f"Answer: {faq['answer']}"
        )

        chunks.append({
            "id": f"{pid}_faq_{i}",
            "text": faq_text,
            "metadata": {
                "product_id": pid,
                "chunk_type": "faq",
                "category": product["category"],
                "price": product.get("price", 0),
            },
        })

    return chunks

