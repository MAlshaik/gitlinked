async function updateUserSearchHist(userId, newSearch) {
    const { data, error } = await supabase
      .from('users')
      .update({ searchhist: supabase.raw(`array_append(searchhist, ?)`, [newSearch]) })
      .eq('user_id', userId);
  
    if (error) {
      console.error('Error updating search history:', error);
      return null;
    }
  
    return data;
  }
  