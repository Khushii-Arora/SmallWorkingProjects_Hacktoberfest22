import React , {useContext}from 'react'
import {GlobalContext} from '../Context/GlobalState.js'
import Transaction from './Transaction.js'

const TransactionList = () => {
    const {transactions} = useContext(GlobalContext)
    return (
        <div>
            <h3>History</h3>
            <ul className="list">
            {transactions.map((transaction)=> {
                return (
                    <Transaction transaction={transaction} key={transaction.id}/>
                );
            })}
               
            </ul>
        </div>
    )
}

export default TransactionList