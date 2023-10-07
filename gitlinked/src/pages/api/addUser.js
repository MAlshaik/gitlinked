async function addUser(email) {
    const { data, error } = await supabase
      .from('users')
      .insert([
        {  email: email},
      ]);
  
    if (error) {
      console.error('Error inserting user:', error);
      return null;
    }
  
    return data;
  }
  