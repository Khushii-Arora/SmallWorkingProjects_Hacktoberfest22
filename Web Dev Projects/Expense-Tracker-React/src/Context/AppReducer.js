// // eslint-disable-next-line import/no-anonymous-default-export
// export default (state, action) => {
//     switch (action.type) {
//         // case value:
            
//         //     break;
    
//         default:
//             return state;
//     }
// // }

// eslint-disable-next-line import/no-anonymous-default-export
export default (state, action) => {
    switch (action.type) {
        case "DELETE_TRANSACTION":
            
            return{
                ...state,
                transactions: state.transactions.filter(transaction => transaction.id !== action.payload)
            }
        
            case "ADD_TRANSACTION":
            
                return{
                    ...state,
                    transactions: [action.payload , ...state.transactions]
                }
    
        default:
            return state;
    }
}

// eslint-disable-next-line import/no-anonymous-default-export
// export default (state, action) => {
//     switch(action.type) {
//         case 'DELETE_TRANSACTION':
//             return {
//               ...state,
//               transactions: state.transactions.filter(transaction => transaction.id !== action.payload)
//             }
//           case 'ADD_TRANSACTION':
//             return {
//               ...state,
//               transactions: [action.payload, ...state.transactions]
//             }
//           default:
//             return state;
//     }
// }