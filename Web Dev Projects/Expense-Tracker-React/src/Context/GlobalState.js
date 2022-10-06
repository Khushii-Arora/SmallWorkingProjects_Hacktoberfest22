import React, { createContext, useReducer } from 'react';
import AppReducer from './AppReducer';

const initialState = {
    transactions: [
        {
        id:1,
        text: 'Income', 
        amount: 2000
        },
    ]
}

export const GlobalContext = createContext(initialState);

export const GlobalProvider = ({children}) => {
    const [state, dispatch] = useReducer(AppReducer, initialState);
    const deleteTransaction =(id) => {
        dispatch({
            type: 'DELETE_TRANSACTION',
            payload: id
        })
    }

    const addTransaction =(transaction) => {
        dispatch({
            type: 'ADD_TRANSACTION',
            payload: transaction
        })
    }

    return (
        <GlobalContext.Provider value={{
            transactions: state.transactions,
            deleteTransaction,
            addTransaction
        }}>
            {children}
        </GlobalContext.Provider>
    )
}