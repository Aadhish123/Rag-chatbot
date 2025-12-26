import logging
from logging_config import setup_logging
from kg_grounding import grounded_answer

# Setup logging once
setup_logging()

def ask(query):
    logging.info(f"Query received: {query}")

    result = grounded_answer(query)

    if "document_id" in result:
        logging.info(
            f"Answer returned from doc {result['document_id']} "
            f"page {result['page_number']}"
        )
        print("\nAnswer:")
        print(result["answer"])
        print(f"(Source: Page {result['page_number']})")
    else:
        logging.warning("Query rejected: no verified answer")
        print("\nAnswer:")
        print(result["answer"])


if __name__ == "__main__":
    print("Dynamic Document QA System")
    print("Type your question below. Type 'exit' to quit.\n")

    while True:
        query = input("Ask a question: ").strip()

        if query.lower() == "exit":
            print("Exiting application.")
            logging.info("Application exited by user.")
            break

        if not query:
            print("Please enter a valid question.")
            continue

        ask(query)
