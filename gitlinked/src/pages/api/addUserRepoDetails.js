import supabase from "../supabaseClient";
export  default async function addUserRepoDetails(req, res){

    const { data, error } = await supabase
          .from('users_descriptive')
          .insert([
            {id: req.body.id,  repos: req.body.repos, 
              interest: req.body.interest, 
              availibility: req.body.availibility,
            skills: req.body.skills },
          ]);
      
        if (error) {
          console.error('Error inserting user:', error);
          return null;
        }
      
        res.status(200).json(data);
      };

