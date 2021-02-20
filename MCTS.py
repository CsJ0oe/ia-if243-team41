from Goban import Board
import random
import math

class MCTSNode(object):
    def __init__(self, unvisited_moves, parent=None, move=None):
        self.parent = parent
        self.move = move
        self.win_counts = {
            Board._BLACK: 0,
            Board._WHITE: 0,
        }
        self.num_rollouts = 0
        self.children = []
        self.unvisited_moves = unvisited_moves

    def add_random_child(self, board):
        index = random.randint(0, len(self.unvisited_moves)-1)
        new_move = self.unvisited_moves.pop(index)
        while board.push(new_move) == False:
            board.pop()
            if not self.can_add_child():
                return self
            index = random.randint(0, len(self.unvisited_moves)-1)
            new_move = self.unvisited_moves.pop(index)
        new_node = MCTSNode(board.weak_legal_moves(), self, new_move)
        #board.pop()
        self.children.append(new_node)
        return new_node

    def record_win(self, winner):
        if winner == "1-0": 
            self.win_counts[Board._WHITE] += 1
        elif winner == "0-1":
            self.win_counts[Board._BLACK] += 1
        self.num_rollouts += 1

    def can_add_child(self):
        return len(self.unvisited_moves) > 0

    def is_terminal(self, board):
        return board.is_game_over()

    def winning_frac(self, player):
        return float(self.win_counts[player]) / float(self.num_rollouts)


class MCTSAgent():
    def __init__(self, num_rounds=1000, temperature=1.4):
        self.num_rounds = num_rounds
        self.temperature = temperature

    def select_move(self, board):
        root = MCTSNode(board.weak_legal_moves())
        # add nodes (at least 10,000 rollouts per turn)
        for i in range(self.num_rounds):
            node = root
            while (not node.can_add_child()) and (not board.is_game_over()):
                node = self.select_child(node, board)
                #board.push(node.move)
            if node.can_add_child() and not board.is_game_over():
                node = node.add_random_child(board)
                #board.push(node.move)
            winner = self.simulate_random_game(board)
            while node is not None:
                node.record_win(winner)
                if node.parent != None:
                    board.pop()
                node = node.parent
        # debug
  from Goban import Board
import random
import math

class MCTSNode(object):
    def __init__(self, unvisited_moves, parent=None, move=None):
        self.parent = parent
        self.move = move
        self.win_counts = {
            Board._BLACK: 0,
            Board._WHITE: 0,
        }
        self.num_rollouts = 0
        self.children = []
        self.unvisited_moves = unvisited_moves

    def add_random_child(self, board):
        index = random.randint(0, len(self.unvisited_moves)-1)
        new_move = self.unvisited_moves.pop(index)
        while board.push(new_move) == False:
            board.pop()
            if not self.can_add_child():
                return self
            index = random.randint(0, len(self.unvisited_moves)-1)
            new_move = self.unvisited_moves.pop(index)
        new_node = MCTSNode(board.weak_legal_moves(), self, new_move)
        #board.pop()
        self.children.append(new_node)
        return new_node

    def record_win(self, winner):
        if winner == "1-0": 
            self.win_counts[Board._WHITE] += 1
        elif winner == "0-1":
            self.win_counts[Board._BLACK] += 1
        self.num_rollouts += 1

    def can_add_child(self):
        return len(self.unvisited_moves) > 0

    def is_terminal(self, board):
        return board.is_game_over()

    def winning_frac(self, player):
        return float(self.win_counts[player]) / float(self.num_rollouts)


class MCTSAgent():
    def __init__(self, num_rounds=1000, temperature=1.4):
        self.num_rounds = num_rounds
        self.temperature = temperature

    def select_move(self, board):
        root = MCTSNode(board.weak_legal_moves())
        # add nodes (at least 10,000 rollouts per turn)
        for i in range(self.num_rounds):
            node = root
            while (not node.can_add_child()) and (not board.is_game_over()):
                node = self.select_child(node, board)
                #board.push(node.move)
            if node.can_add_child() and not board.is_game_over():
                node = node.add_random_child(board)
                #board.push(node.move)
            winner = self.simulate_random_game(board)
            while node is not None:
                node.record_win(winner)
                if node.parent != None:
                    board.pop()
                node = node.parent
        # debug
        scored_moves = [(child.winning_frac(board.next_player()), child.move, child.num_rollouts)
                        for child in root.children]
        scored_moves.sort(key=lambda x: x[0], reverse=True)
        for s, m, n in scored_moves[:10]:
            print('%s - %.3f (%d)' % (m, s, n))
        # pick best node
        best_move = None
        best_pct = -1.0
        for child in root.children:
            child_pct = child.winning_frac(board.next_player())
            if child_pct > best_pct:
                best_pct = child_pct
                best_move = child.move
        print('Select move %s with win pct %.3f' % (best_move, best_pct))
        return best_move

    def select_child(self, node, board):
        # upper confidence bound for trees (UCT) metric
        total_rollouts = sum(child.num_rollouts for child in node.children)
        log_rollouts = math.log(total_rollouts)

        best_score = -1
        best_child = None
        # loop over each child.
        for child in node.children:
            # calculate the UCT score.
            win_percentage = child.winning_frac(board.next_player())
            exploration_factor = math.sqrt(log_rollouts / child.num_rollouts)
            uct_score = win_percentage + self.temperature * exploration_factor
            # Check if this is the largest we've seen so far.
            if uct_score > best_score:
                best_score = uct_score
                best_child = child
        board.push(best_child.move)
        return best_child

    @staticmethod
    def simulate_random_game(board):
        nb_push = 0
        while not board.is_game_over():
            moves = board.weak_legal_moves()
            move = random.choice(moves)
            while board.push(move) == False:
                board.pop()
                move = random.choice(moves)
            nb_push += 1
        winner = board.result()
        while nb_push > 0:
            board.pop()
            nb_push -= 1
        return winner
