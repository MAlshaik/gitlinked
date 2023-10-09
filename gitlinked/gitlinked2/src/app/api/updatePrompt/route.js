import supabase from "@/app/supabaseClient";
import { NextResponse } from "next/server";

export async function POST(req){

    const body = await req.json();

    try {
        const {data, error} = await supabase
        .from('users')
        .update({ prompts: supabase.raw(`array_append(prompts, ?)`, [body.newSearch])})
        .ewq('id', body.id);

        if(error){
            throw error;
        }
        return NextResponse.json({message:"success"});
    }catch (error) {
        console.error('Error updating:', error.message || error);
        return NextResponse.json({error : 'Failed to update'});
    }

}