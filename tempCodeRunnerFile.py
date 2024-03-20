#LAYER 2
        # if(self.current_symbol == 'D' or self.current_symbol == 'R' or self.current_symbol == 'U'):
        # 	prediction = {}
        # 	prediction['D'] = result_dru[0][0]
        # 	prediction['R'] = result_dru[0][1]
        # 	prediction['U'] = result_dru[0][2]
        # 	prediction = sorted(prediction.items(), key=operator.itemgetter(1), reverse=True)
        # 	self.current_symbol = prediction[0][0]

        # if(self.current_symbol == 'D' or self.current_symbol == 'I' or self.current_symbol == 'K' or self.current_symbol == 'T'):
        # 	prediction = {}
        # 	prediction['D'] = result_tkdi[0][0]
        # 	prediction['I'] = result_tkdi[0][1]
        # 	prediction['K'] = result_tkdi[0][2]
        # 	prediction['T'] = result_tkdi[0][3]
        # 	prediction = sorted(prediction.items(), key=operator.itemgetter(1), reverse=True)
        # 	self.current_symbol = prediction[0][0]

        # if(self.current_symbol == 'M' or self.current_symbol == 'N' or self.current_symbol == 'S'):
        # 	prediction1 = {}
        # 	prediction1['M'] = result_smn[0][0]
        # 	prediction1['N'] = result_smn[0][1]
        # 	prediction1['S'] = result_smn[0][2]
        # 	prediction1 = sorted(prediction1.items(), key=operator.itemgetter(1), reverse=True)
        # 	if(prediction1[0][0] == 'S'):
        # 		self.current_symbol = prediction1[0][0]
        # 	else:
        # 		self.current_symbol = prediction[0][0]
        # if(self.current_symbol == 'blank'):
        #     for i in ascii_uppercase:
        #         self.ct[i] = 0
        # self.ct[self.current_symbol] += 1
        # if(self.ct[self.current_symbol] > 60):