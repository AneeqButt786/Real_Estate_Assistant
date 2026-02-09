from agents import Agent

mortgage_checker_agent = Agent(name="Mortgage Eligibility Checker", instructions="Determine mortgage eligibility. Output: Eligibility Estimate, Reasoning, Advice.", model="gpt-4o-mini")
property_recommender_agent = Agent(name="Property Recommender", instructions="Match preferences with listings. Output: Property #1, Property #2.", model="gpt-4o-mini")
multilingual_support_agent = Agent(name="Multilingual Buyer Support", instructions="Support buyers in preferred language.", model="gpt-4o-mini")

property_agent = Agent(
    name="Intelligent Property Buying Assistant",
    instructions="Route: check_mortgage_eligibility for financial, recommend_properties for search, translate_property_details for translations.",
    model="gpt-4o-mini",
    tools=[
        mortgage_checker_agent.as_tool(tool_name="check_mortgage_eligibility", tool_description="Check mortgage eligibility."),
        property_recommender_agent.as_tool(tool_name="recommend_properties", tool_description="Suggest properties."),
        multilingual_support_agent.as_tool(tool_name="translate_property_details", tool_description="Translate property info."),
    ],
)
