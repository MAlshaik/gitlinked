import { NextResponse } from "next/server";
import supabase from "../../supabaseClient";

export async function POST(req){
    const body = await req.json()
    console.log(body);
    try{
    const {data, error } = await supabase
    .from('users_descriptive')
    .update({skills : body.skills})
    .eq('id', body.id);

    if (error){
        throw error;
    }

    return NextResponse.json({success:true, message:'Updated skills'});
    }catch(error){
        console.log(`Eror updating skills ${error}`);
        return NextResponse.json({error: 'Failed to updated skills'});
    }
}