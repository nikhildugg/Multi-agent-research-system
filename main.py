"""
DuggResearchMind - CLI Research Entrypoint
Author: Nikhil (github.com/nikhildugg)

Coordinates the multi-agent search, scraping, drafting, and critique pipeline.
"""

from dugg_agents import build_reader_agent, build_search_agent, writer_chain, critic_chain

def run_research_pipeline(topic: str) -> dict:
    """Runs the full multi-agent research pipeline for a given topic and returns results."""
    state = {}

    # Step 1: Search Agent Execution
    print("\n" + "=" * 50)
    print(" [Step 1] - Search Agent is finding resources... ")
    print("=" * 50)

    search_agent = build_search_agent()
    search_result = search_agent.invoke({
        "messages": [("user", f"Find recent, reliable and detailed information about: {topic}")]
    })
    state["search_results"] = search_result['messages'][-1].content
    print("\nSearch Results Gathered:\n", state['search_results'])

    # Step 2: Reader Agent Execution
    print("\n" + "=" * 50)
    print(" [Step 2] - Reader Agent is parsing top sources... ")
    print("=" * 50)

    reader_agent = build_reader_agent()
    reader_result = reader_agent.invoke({
        "messages": [("user",
            f"Based on the following search results about '{topic}', "
            f"pick the most relevant URL and scrape it for deeper content.\n\n"
            f"Search Results:\n{state['search_results'][:800]}"
        )]
    })
    state['scraped_content'] = reader_result['messages'][-1].content
    print("\nDeep Scraped Content:\n", state['scraped_content'])

    # Step 3: Writer Chain Execution
    print("\n" + "=" * 50)
    print(" [Step 3] - Writer Chain is drafting the report... ")
    print("=" * 50)

    research_combined = (
        f"SEARCH RESULTS:\n{state['search_results']}\n\n"
        f"DETAILED SCRAPED CONTENT:\n{state['scraped_content']}"
    )

    state["report"] = writer_chain.invoke({
        "topic": topic,
        "research": research_combined
    })
    print("\nDrafted Research Report:\n", state['report'])

    # Step 4: Critic Chain Execution
    print("\n" + "=" * 50)
    print(" [Step 4] - Critic Chain is reviewing & grading the report... ")
    print("=" * 50)

    state["feedback"] = critic_chain.invoke({
        "report": state['report']
    })
    print("\nCritic Feedback & Review:\n", state['feedback'])

    return state

if __name__ == "__main__":
    target_topic = input("\nEnter a research topic to search and analyze: ")
    run_research_pipeline(target_topic)
