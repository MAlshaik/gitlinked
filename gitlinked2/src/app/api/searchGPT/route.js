import { NextResponse } from "next/server";

export async function POST(req) {
  const body = await req.json();
  /*
    if (req.method !== 'POST') {
      return res.status(405).json({ error: 'Method not allowed' });
    }
  */
    await fetch('', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(body)
    })
    .then(response => response.json)
    .then(data => {
      console.log('Success:', data);
    })
    .catch(error => {
      console.error(error);
      return NextResponse.json({message:'Failed'});
    })
  return NextResponse.json({message : 'success'});
  
  }
  