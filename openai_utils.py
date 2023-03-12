import openai

def create_table_definition_prompt(df, table_name):
    """This function creates a prompt for the OpenAI API to generate SQL queries.

    Args:
        df (dataframe): pd.DataFrame object to automatically extract the table columns
        table_name (string): Name of the table within hte database

    Returns: string containing thte prompt for OpenAI
    """

    prompt = '''### sqlite table, with its properties:
    #
    # {}({})
    #
    '''.format(table_name, ",".join(str(x) for x in df.columns))

    return prompt

def user_query_input():
    """Ask the user what they want to know about the data.

    Returns:
        string: User Input
    """
    user_input = input("Tell OpenAI what you want to know about the data: ")
    return user_input

def combine_prompts(fixed_sql_prompt, user_query):
    """Combine the fixed SQL prompt with the user query.

    Args:
        fixed_sql_prompt (string): Fixed SQL prompt
        user_query (string): User query

    Returns:
        string: Combined prompt
    """
    final_user_input = f"### A query to answer: {user_query}\nSELECT"
    return fixed_sql_prompt + final_user_input

def send_to_openai(prompt):
    """Send the prompt to OPenAI

    Args:
        prompt (string): Prompt to send to OpenAI

    Returns:
        string: Response from OpenAI
    """
    response = openai.Completion.create(
        engine="code-davinci-002",
        prompt=prompt,
        temperature=0,
        max_tokens=150,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["#", ";"]
    )
    return response