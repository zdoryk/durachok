
let mutations = {
    START_GAME: (state) => {
        state.game_started = true
    },

    INITIAL_SET_UP: (state, data) => {
        state.opponent_cards_amount = data.bot_hand_size
        state.deck_amount = data.deck_size
        state.muck_amount = data.discard_size
        state.trump.card_rank = data.trump.card_rank
        state.player.is_player_active = data.player_state
        state.trump.card_suit = data.trump.card_suit.toLowerCase()
        state.cards = data.player_cards.map(function (card, index) {
            card.card_index = index
            // card.card_height = 120
            // card.card_suit = card.card_suit.toLowerCase()
            return card
        })
        // state.cards = data.player_cards
    },

    SET_PLAYER_DEFEND: (state) => {
        state.player.player_state = 2
        state.player.is_player_active = true
    },

    GET_TABLE_MUTATION: (state, data) => {
        state.cards_on_bot = data.cards_on_bot
        state.cards_on_top = data.cards_on_top
    },

    SET_PLAYER_HAND: (state, cards) => {
        state.cards = cards.map(function (card, index) {
            card.card_index = index
            return card
        })
    },

    THROW_CARD: (state, card) => {
        state.cards_on_bot.push(card)
    },

    DEFEND_WITH_CARD: (state, card) => {
        state.cards_on_top.push(card)
    },

    SET_USED_CARD_RANKS: (state, card) => {
        state.used_card_ranks.push(card.card_rank)
        state.used_card_ranks = [...new Set(state.used_card_ranks)]
    },

    DELETE_CARD_FROM_HAND: (state, card) => {
        state.cards = JSON.parse(
            JSON.stringify(
                state.cards.filter(card_in_hand => card_in_hand.card_index !== card.card_index)))
    },

    SET_NEW_INDEXES: (state) => {
        for (let i = 0; i < state.cards.length; i++){
            state.cards[i].card_index = i
        }
    },

}




export default mutations
