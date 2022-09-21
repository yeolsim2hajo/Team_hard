function solution(board, moves) {
  var answer = 0;
  var lst = [];
   for(let i = 0; i < moves.length; i++) {
       var move = moves[i] - 1; 
       for(let j = 0; j < board.length; j++) {
           var rst = board[j][move];
           if (rst) {
               board[j][move] = 0;
               if (lst.length !== 0 && lst[lst.length-1] === rst) {
                   lst.pop()
                   answer += 2;
               } else {
                   lst.push(rst);
               }
               break;
           };
       };
   }
  return answer;
}