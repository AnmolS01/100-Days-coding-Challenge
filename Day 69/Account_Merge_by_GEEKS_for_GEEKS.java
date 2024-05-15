import java.util.*;

class Solution {
    // Function to find the parent of a node in the union-find data structure.
    private String find(String s, Map<String, String> p) {
        // If the parent of the node is the node itself, we return the node.
        // Otherwise, we recursively find the parent of the parent until we reach the node whose parent is itself.
        return p.get(s).equals(s) ? s : find(p.get(s), p);
    }
    
    // Function to merge the accounts using union-find data structure.
    public List<List<String>> accountsMerge(List<List<String>> accounts) {
        // Creating maps for owner, parent, and unions.
        Map<String, String> owner = new HashMap<>();
        Map<String, String> parents = new HashMap<>();
        Map<String, Set<String>> unions = new HashMap<>();
        
        // Looping through all the accounts to initialize the maps.
        for (List<String> account : accounts) {
            // Setting the parent of each email as the email itself.
            // Setting the owner of each email as the first email in the account.
            for (int j = 1; j < account.size(); j++) {
                parents.put(account.get(j), account.get(j));
                owner.put(account.get(j), account.get(0));
            }
        }
        
        // Looping through all the accounts to merge the emails.
        // Merging is done by finding the parent of each email and updating the parent of all emails in the account to the same parent.
        for (List<String> account : accounts) {
            String p = find(account.get(1), parents);
            for (int j = 2; j < account.size(); j++)
                parents.put(find(account.get(j), parents), p);
        }
        
        // Looping through all the accounts to group the emails by their parent.
        // We add each email to the set of emails for its parent.
        for (List<String> account : accounts) {
            for (int j = 1; j < account.size(); j++) {
                String parent = find(account.get(j), parents);
                unions.computeIfAbsent(parent, k -> new HashSet<>()).add(account.get(j));
            }
        }

        // Creating the result list of lists.
        // For each group of emails (union), we convert the set of emails to a list and insert the owner as the first element of the list.
        List<List<String>> ans = new ArrayList<>();
        for (Map.Entry<String, Set<String>> entry : unions.entrySet()) {
            List<String> res = new ArrayList<>(entry.getValue());
            res.add(0, owner.get(entry.getKey()));
            ans.add(res);
        }
        // Returning the result list of lists.
        return ans;
    }
} 
