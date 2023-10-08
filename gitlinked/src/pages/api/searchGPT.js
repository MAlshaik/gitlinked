export default async function handler(req, res) {
    if (req.method !== 'POST') {
      return res.status(405).json({ error: 'Method not allowed' });
    }
  
    const gpt_prompt = `Extract interest(into string), skills into list of strings and availability as an int. The return from you must only include what is asked(no advice). Also it needs to be in a very easy format to extract. Availability will have two values, lower and higher. Make sure to separate the availability of hours into two rows so it is easier to extract them. Add separators to make sure that its easy to extract the variables:`;
  
    try {
      const response = await fetch('https://api.openai.com/v1/chat/completions', {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${process.env.OPENAI_API_KEY}`,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          prompt: gpt_prompt + "\n" + req.body.prompt,
          max_tokens: 500,
          model: "gpt-3.5-turbo"
        }),
      });
  
      const data = await response.json();
  
      if (!response.ok) {
        throw new Error(data.error || 'OpenAI API call failed');
      }
  
      return res.status(200).json(data);
  
    } catch (error) {
      console.error('Error:', error.message);
      return res.status(500).json({ error: error.message });
    }
  }
  