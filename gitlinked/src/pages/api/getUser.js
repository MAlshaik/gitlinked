async function getUser(email) {
    const { data, error } = await supabase
      .from('user')
      .select('*')
      .eq('user_id', email)
      .single();
  
    if (error) {
      console.error('Error fetching user:', error);
      return null;
    }
  
    return data;
  }