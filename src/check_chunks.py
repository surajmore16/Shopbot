


from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))

from data.products import PRODUCTS
from src.chunker import product_to_chunks
all_chunks = []

for product in PRODUCTS:
    chunks = product_to_chunks(product)
    all_chunks.extend(chunks)
    print(f"{product['name']}: {len(chunks)} chunks")

print(f"\nTotal chunks: {len(all_chunks)}")
print(chunks)

# {
#   "total_chunks": 30,
#   "chunks": [
#     {
#       "id": "p005_identity",
#       "text": "Classic Denim Jeans. Straight-fit denim jeans crafted from durable stretch denim. Designed for everyday comfort while maintaining a clean, timeless look. Category: jeans. Fabric: 98% cotton, 2% elastane. Occasion: casual, daily wear, travel.",
#       "metadata": {
#         "product_id": "p005",
#         "chunk_type": "identity",
#         "category": "jeans",
#         "price": 2199
#       }
#     },
#     {
#       "id": "p005_variants",
#       "text": "Classic Denim Jeans is available in colours: dark blue, black, stone wash. Available sizes: 28, 30, 32, 34, 36, 38. Price: ₹2199. Stock status: in stock.",
#       "metadata": {
#         "product_id": "p005",
#         "chunk_type": "variants",
#         "category": "jeans",
#         "price": 2199
#       }
#     },
#     {
#       "id": "p005_policy",
#       "text": "Return and exchange policy for Classic Denim Jeans: Returns accepted within 14 days. Item must be unworn and returned in original condition. Exchange: free size exchange within 14 days of delivery.",
#       "metadata": {
#         "product_id": "p005",
#         "chunk_type": "policy",
#         "category": "jeans",
#         "price": 2199
#       }
#     },
#     {
#       "id": "p005_care",
#       "text": "Care instructions for Classic Denim Jeans: Wash inside out with similar colours. Do not bleach. Tumble dry low or line dry.",
#       "metadata": {
#         "product_id": "p005",
#         "chunk_type": "care",
#         "category": "jeans",
#         "price": 2199
#       }
#     },
#     {
#       "id": "p005_faq_0",
#       "text": "Question about Classic Denim Jeans: Do these jeans stretch over time? Answer: The elastane blend provides slight stretch for comfort while helping the jeans retain their shape.",
#       "metadata": {
#         "product_id": "p005",
#         "chunk_type": "faq",
#         "category": "jeans",
#         "price": 2199
#       }
#     },
#     {
#       "id": "p005_faq_1",
#       "text": "Question about Classic Denim Jeans: Are these suitable for travel? Answer: Yes. The comfortable fit and durable fabric make them well-suited for travel and everyday use.",
#       "metadata": {
#         "product_id": "p005",
#         "chunk_type": "faq",
#         "category": "jeans",
#         "price": 2199
#       }
#     }
#   ]
# }