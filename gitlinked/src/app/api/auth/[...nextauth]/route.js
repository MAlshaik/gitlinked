import NextAuth from "next-auth";
import GitHubProvider from "next-auth/providers/github";
import supabase from "../../../supabaseClient";
const { spawn } = require('child_process');

import * as Sentry from "@sentry/nextjs"


Sentry.captureMessage("hello from route.js");

export const authOptions = {

        providers: [
            GitHubProvider({
                clientId: process.env.GITHUB_ID,
                clientSecret: process.env.GITHUB_SECRET,
                redirectUri: process.env.GITHUB_REDIRECT_URI
            }),
        ],
        debug: process.env.NODE_ENV === "development",
        secret: process.env.AUTH_SECRET,
        jwt: {
            secret: process.env.JWT_SECRET,
        },
        callbacks: {
            async signIn(user, account, profile) {
                console.log("User Object:", user.profile.login);
                
                const existingUser = await getUser(user.user.id);

                if (!existingUser) {
                  await addUser(user.user.id, user.profile.login, user.user.email);
                  
                  const body = {
                    'id': user.user.id,
                    'username': user.profile.login
                  }


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
                  })
                  .catch(error => {
                    console.error('Error:', error); // Handle errors
                  });
                  
            }
                console.log(`Signed in as ${user.profile.login}`);
                return true; // return true to continue the sign-in process, otherwise it will be stopped
              },
            
            async redirect(url, baseUrl) {
                return "/";
            },
        },
    };

    async function addUser(userId, username,email) {
        const { data, error } = await supabase
          .from('users')
          .insert([
            {id: userId, username:username, email: email },
          ]);
      
        if (error) {
          console.error('Error inserting user:', error);
          return null;
        }
      
        return data;
      }
      
      async function getUser(id) {
        const { data, error } = await supabase
          .from('users')
          .select('*')
          .eq('id', id)
          .single();
      
        if (error) {
          console.error('Error fetching user:', error);
          return null;
        }
      
        return data;
      }
    
export const handler = NextAuth(authOptions);
export {handler as GET, handler as POST};
