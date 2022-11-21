let getters = {
    CARDS(state){
        return state.cards
    },
    BOTTOM_CARDS(state){
        return state.cards_on_bot
    },
    TOP_CARDS(state){
        return state.cards_on_top
    },
    CARD_VALUES(state){
        return state.card_values
    },
    PLAYER(state){
        return state.player
    },
    DECK_AMOUNT(state){
        return state.deck_amount
    },
    TRUMP(state){
        return state.trump
    },
    MUCK_AMOUNT(state){
        return state.muck_amount
    },
    OPPONENT_CARDS_AMOUNT(state){
        return state.opponent_cards_amount
    }


}

export default getters;
