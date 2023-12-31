import supabase from "../../supabaseClient";
import { NextResponse } from "next/server";

import * as Sentry from "@sentry/nextjs";

export async function POST(req){

    Sentry.captureMessage('hello from addUser');

    const body = await req.json()
    
    if (req.method !== 'POST') {
      return NextResponse.send({ error: 'Method not allowed' });
    }
    

    const { data, error } = await supabase
      .from('contributors')
      .insert([
        {id: body.id, repos:body.repos, username:body.username},
      ]);

    if (error) {
      console.error('Error inserting user:', error);
      return NextResponse.send({ error: 'Error inserting user' });
    }
  
    return NextResponse.json({ success: true });
    
}

