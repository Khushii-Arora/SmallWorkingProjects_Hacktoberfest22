import React , {useContext} from 'react'
import {GlobalContext} from '../Context/GlobalState.js'

const IncomeExpenses = () => {
    const {transactions} = useContext(GlobalContext)

    const amounts = transactions.map(transaction => transaction.amount);

    const income = amounts
         .filter(item => item > 0)
         .reduce((acc, item) => (acc += item), 0);

    const expense = (
        amounts.filter(item => item < 0).reduce((acc, item) => (acc += item), 0) *
    -1
  );
    return (
        <div className="inc-exp-container">
            <div>
                <h4>Income</h4>
                <p id="money-plus" className="money plus">+${income}</p>
            </div>
            <div>
                <h4>Expense</h4>
                <p id="money-minus" className="money minus">-${expense}</p>
            </div>
        </div>
    )
}

export default IncomeExpenses
