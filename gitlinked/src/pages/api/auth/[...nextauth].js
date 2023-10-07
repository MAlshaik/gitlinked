import NextAuth from "next-auth";
import Github from "next-auth/providers/github";
import GitHubProvider from "next-auth/providers/github";
import supabase from "../../supabaseClient";
const { spawn } = require('child_process');

export default (req, res) =>
    NextAuth(req, res, {
        providers: [
            GitHubProvider({
                clientId: process.env.GITHUB_CLIENT_ID,
                clientSecret: process.env.GITHUB_CLIENT_SECRET,
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
                
                const existingUser = await getUser(user.user.email);
        
                if (!existingUser) {
                  await addUser(user.user.id, user.profile.login, user.user.email);
                  const pythonProcess = spawn('python', ['get_info.py', '--id', user.user.id, '--username', user.profile.login]);
                  
                  pythonProcess.stdout.on('data', (data) => {
                    // Handle stdout data (output from the Python script)
                    console.log(data.toString());
                    // If you still want to write this data to output.txt, use the fs module.
                });
                
                pythonProcess.stderr.on('data', (data) => {
                    // Handle any errors
                    console.error(`Python error: ${data}`);
                });
                
                pythonProcess.on('close', (code) => {
                    if (code !== 0) {
                        console.log(`Python script exited with code ${code}`);
                    }
                });
                
                
                }
        
                return true; // return true to continue the sign-in process, otherwise it will be stopped
              },
            
            async redirect(url, baseUrl) {
                return "/";
            },
        },
    });

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
      
      async function getUser(email) {
        const { data, error } = await supabase
          .from('users')
          .select('*')
          .eq('email', email)
          .single();
      
        if (error) {
          console.error('Error fetching user:', error);
          return null;
        }
      
        return data;
      }

