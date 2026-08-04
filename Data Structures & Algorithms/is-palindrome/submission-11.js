class Solution {
    isPalindrome(s) {
        // 1. Zamień na małe litery
        // 2. Wyrzuć wszystko co NIE jest literą lub cyfrą (regex: /[^a-z0-9]/g)
        const cleanStr = s.toLowerCase().replace(/[^a-z0-9]/g, '');
        
        // 3. Porównaj string z jego odwróconą wersją
        return cleanStr === cleanStr.split('').reverse().join('');
    }
}