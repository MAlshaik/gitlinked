const { spawn } = require('child_process');
import { NextResponse } from 'next/server';
export async function POST(req) {
    const body = await req.json();

    //remember body.name

    fetch('', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json' // Set the content type to JSON
          },
          body: JSON.stringify(body) // Convert the data to a JSON string
        })
        .then(response => response.json()) // Parse the JSON response
        .then(data => {
          console.log('Success:', data); // Handle the response data
          return NextResponse.json({message:"success"});
        })
        .catch(error => {
          console.error('Error:', error); // Handle errors
          return NextResponse.json({message:'fail'});
        });
        
    

}    
    

