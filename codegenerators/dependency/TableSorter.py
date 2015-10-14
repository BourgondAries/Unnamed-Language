def sortTable(productions, terminals):
	seen = ['ENTER']
	to_process = ['ENTER']
	# Iterate all elements, if they're in the terminal set, just ignore them.
	while to_process:
		processing = to_process.pop()
		start = productions[processing]
		start.sort()
		print("'" + processing + "': " + str(start))
		for i in start:
			for j in i:
				if j not in terminals:
					if j not in seen:
						to_process.insert(0, j)
						seen.append(j)


productions = {
################################################################################ 1
	'ENTER': [
		['ACCESS_SPECIFIER', 'MEMBER_DEFINITION', 'ENTER'],
		['ALIAS_STATEMENT', 'ENTER'],
		['KEYWORD_GRANT', 'IDENTIFIER_CLASS', 'GROUPER_LEFT_BRACE', 'GRANT_LIST', 'GROUPER_RIGHT_BRACE', 'ENTER'],
		[]
	],
################################################################################ 2
	'MEMBER_DEFINITION': [
		['DATA_DECLARATION_STATEMENT'],
		['FUNCTION_SIGNATURE', 'FUNCTION_NAMES', 'GROUPER_LEFT_BRACE', 'STATEMENT_LIST', 'GROUPER_RIGHT_BRACE']
	],
	'ALIAS_STATEMENT': [
		['KEYWORD_ALIAS', 'ALIAS_CORE']
	],
################################################################################ 2.1
	'DATA_DECLARATION_STATEMENT': [
		['VAR_OR_STATIC', 'DATA_DECLARATION_TYPE'],
	],
	'FUNCTION_NAMES': [
		['IDENTIFIER_SUBROUTINE'],
		['IDENTIFIER_PACKAGE'],

		['SYMBOL_PLUS'],
		['SYMBOL_PLUS__PLUS'],
		['SYMBOL_MINUS'],
		['SYMBOL_MINUS__MINUS'],
		['SYMBOL_STAR'],
		['SYMBOL_FORWARD_SLASH'],
		['SYMBOL_PERCENT'],

		['SYMBOL_PLUS__EQUAL'],
		['SYMBOL_MINUS__EQUAL'],
		['SYMBOL_STAR__EQUAL'],
		['SYMBOL_FORWARD_SLASH__EQUAL'],
		['SYMBOL_PERCENT__EQUAL'],
		['SYMBOL_LESS_THAN__LESS_THAN__EQUAL'],
		['SYMBOL_GREATER_THAN__GREATER_THAN__EQUAL'],

		['SYMBOL_EQUAL__EQUAL'],
		['SYMBOL_EXCLAMATION_MARK__EQUAL'],
		['SYMBOL_LESS_THAN'],
		['SYMBOL_GREATER_THAN'],
		['SYMBOL_LESS_THAN__EQUAL'],
		['SYMBOL_GREATER_THAN__EQUAL'],

		['SYMBOL_LESS_THAN__LESS_THAN'],
		['SYMBOL_GREATER_THAN__GREATER_THAN'],
	],
	'ALIAS_CORE': [
		['GROUPER_LEFT_BRACE', 'ALIAS_TRAILS', 'GROUPER_RIGHT_BRACE'],
		['ALIAS_TRAIL', 'SYMBOL_SEMICOLON__PRUNE']
	],
################################################################################ 2.2
	'VAR_OR_STATIC': [
		['KEYWORD_VAR'],
		['KEYWORD_STATIC'],
	],
	'ALIAS_TRAILS': [
		['ALIAS_TRAIL', 'SYMBOL_SEMICOLON__PRUNE', 'ALIAS_TRAILS'],
		[]
	],
	'ALIAS_TRAIL': [
		['IDENTIFIER_CLASS', 'SYMBOL_EQUAL', 'TYPE'],
		['IDENTIFIER_PACKAGE', 'SYMBOL_EQUAL', 'IDENTIFIER_PACKAGE'],
	],
################################################################################ 3
# Naming subsytem
################################################################################
	'VARIABLE_NAMES': [
		['FUNCTION_NAMES'],
		['IDENTIFIER_VARIABLE'],
	],

	'DATA_NAMES': [
		['IDENTIFIER_VARIABLE'],
		['IDENTIFIER_PACKAGE']
	],
	# Function names can be any subroutine or package name, as well as any valid symbol.

################################################################################ 3
# End Naming subsytem
################################################################################ 3
################################################################################ 3
# Type subsystem
# External to subsystem: OR_EXPRESSION, ARGUMENT_LIST
# Defines types: ref ptr ptr const ptr const [5, ptr ([3, 8u] out:)]
################################################################################
	'TYPE': [
		['ARRAY'],
		['BASIC_TYPE'],
		['FUNCTION_SIGNATURE'],
		['KEYWORD_CONST', 'TYPE_AFTER_CONST'],
		['KEYWORD_PTR', 'TYPE_AFTER_PTR'],
		['KEYWORD_REF', 'TYPE_AFTER_REF'],
		['TYPE_EXPRESSION'],
	],
############################################################################### 4
	'ARRAY': [
		['GROUPER_LEFT_BRACKET', 'INTEGER_LITERAL', 'SYMBOL_COMMA__PRUNE', 'TYPE', 'GROUPER_RIGHT_BRACKET']
	],
	'BASIC_TYPE': [
		['IDENTIFIER_CLASS', 'OPTIONAL_TEMPLATE'],
		['IDENTIFIER_PACKAGE', 'SYMBOL_DOT__PRUNE', 'IDENTIFIER_CLASS', 'OPTIONAL_TEMPLATE'],
		['KEYWORD_DOUBLE'],
		['KEYWORD_FLOAT'],
		['PRIMITIVE_SIGNED'],
		['PRIMITIVE_UNSIGNED'],
	],
	'TYPE_AFTER_CONST': [
		['ARRAY'],
		['BASIC_TYPE'],
		['KEYWORD_PTR', 'TYPE'],
	],
	'TYPE_AFTER_PTR': [
		['ARRAY'],
		['BASIC_TYPE'],
		['FUNCTION_SIGNATURE'],
		['KEYWORD_CONST', 'TYPE_AFTER_CONST'],
		['KEYWORD_PTR', 'TYPE_AFTER_PTR'],
		['KEYWORD_REF', 'TYPE_AFTER_REF']
	],
	'TYPE_AFTER_REF': [
		['ARRAY'],
		['BASIC_TYPE'],
		['FUNCTION_SIGNATURE'],
		['KEYWORD_CONST', 'TYPE_AFTER_REF_CONST'],
		['KEYWORD_PTR', 'TYPE'],
	],
	'TYPE_EXPRESSION': [
		['KEYWORD_TYPE', 'GROUPER_LEFT_BRACKET', 'VARIABLE_NAMES', 'GROUPER_RIGHT_BRACKET'],
	],
################################################################################ 5
	'OPTIONAL_TEMPLATE': [
		['GROUPER_LEFT_BRACKET', 'TEMPLATE_LIST', 'GROUPER_RIGHT_BRACKET'],
		[]
	],
	'TYPE_AFTER_REF_CONST': [
		['BASIC_TYPE'],
		['KEYWORD_PTR', 'TYPE'],
	],
	'FUNCTION_SIGNATURE': [
		['GROUPER_LEFT_PARENTHESIS', 'ARGUMENT_LIST', 'SYMBOL_COLON__PRUNE', 'ARGUMENT_LIST', 'OPTIONAL_ATTRIBUTE_LIST', 'GROUPER_RIGHT_PARENTHESIS'],
		],
################################################################################ 6
	'TEMPLATE_LIST': [
		['IDENTIFIER_CLASS', 'SYMBOL_COLON__PRUNE', 'TYPE', 'OPTIONAL_TEMPLATE_LIST'],
		['SYMBOL_COLON__PRUNE', 'TYPE', 'OPTIONAL_TEMPLATE_LIST'],
	],
	'OPTIONAL_ATTRIBUTE_LIST': [
		['SYMBOL_COLON__PRUNE', 'ATTRIBUTE_LIST'],
		[]
	],
################################################################################ 7
	'OPTIONAL_TEMPLATE_LIST': [
		['IDENTIFIER_CLASS', 'SYMBOL_COLON__PRUNE', 'TYPE', 'OPTIONAL_TEMPLATE_LIST'],
		['SYMBOL_COLON__PRUNE', 'TYPE', 'OPTIONAL_TEMPLATE_LIST'],
		[]
	],
	'ATTRIBUTE_LIST': [
		['KEYWORD_CONST', 'ATTRIBUTE_LIST_AFTER_CONST'],
		['KEYWORD_PURE'],
		[]
	],
################################################################################ 8
	'ATTRIBUTE_LIST_AFTER_CONST': [
		['KEYWORD_PURE'],
		[]
	],
################################################################################
# End of Type subsystem
################################################################################ 9
	'DATA_DECLARATION_TYPE': [
		['GROUPER_LEFT_BRACE', 'DATA_DECLARATION_LIST', 'GROUPER_RIGHT_BRACE'],
		['TYPE', 'DATA_NAMES', 'OPTIONAL_ASSIGNMENT', 'OPTIONAL_DATA_DECLARATION', 'SYMBOL_SEMICOLON__PRUNE'],
	],
	'ARGUMENT_LIST': [
		['ARGUMENT', 'OPTIONAL_ARGUMENT_LIST'],
		[],
	],
	'OPTIONAL_ASSIGNMENT': [
		['GROUPER_LEFT_PARENTHESIS', 'PARAMETER_LIST', 'GROUPER_RIGHT_PARENTHESIS'],
		['SYMBOL_EQUAL', 'EXPRESSION_EXPRESSION'],
		[]
	],
	'OPTIONAL_DATA_DECLARATION': [
		['SYMBOL_COMMA__PRUNE', 'DATA_NAMES', 'OPTIONAL_ASSIGNMENT', 'OPTIONAL_DATA_DECLARATION'],
		[],
	],
	'ACCESS_SPECIFIER': [
		['KEYWORD_PRIVATE'],
		['KEYWORD_PUBLIC'],
		['KEYWORD_RESTRICTED'],
		[]
	],
	'GRANT_LIST': [
		['VAR_OR_STATIC', 'TYPE', 'VARIABLE_NAMES', 'OPTIONAL_DATA_NAME_LIST', 'SYMBOL_SEMICOLON__PRUNE', 'OPTIONAL_GRANT_LIST'],
		['FUNCTION_SIGNATURE', 'FUNCTION_NAMES', 'OPTIONAL_FUNCTION_NAME_LIST', 'SYMBOL_SEMICOLON__PRUNE', 'OPTIONAL_GRANT_LIST']
	],
################################################################################ 10
	'STATEMENT_LIST': [
		['NO_SEMICOLON_STATEMENT', 'STATEMENT_LIST'],
		['STATEMENT', 'SYMBOL_SEMICOLON__PRUNE', 'STATEMENT_LIST'],
		[]
	],
	'NO_SEMICOLON_STATEMENT': [
		['ALIAS_STATEMENT'],
		['CODE_BLOCK'],
		['DATA_DECLARATION_STATEMENT'],
		['DEFER_STATEMENT'],
		['DO_STATEMENT'],
		['FOR_STATEMENT'],
		['IF_STATEMENT'],
		['STATIC_IF_STATEMENT'],
		['WHILE_STATEMENT'],
	],
	'STATEMENT': [
		['EXPRESSION_EXPRESSION'],
		['GOTO_STATEMENT'],
		['HACK_STATEMENT'],
		['ITER_STATEMENT'],
		['LABEL_STATEMENT'],
		['RETURN_STATEMENT'],
	],
	'PARAMETER_LIST': [
		['DATA_NAMES', 'SYMBOL_COLON__PRUNE', 'EXPRESSION_EXPRESSION', 'OPTIONAL_PARAMETER_LIST'],
		['SYMBOL_COLON__PRUNE', 'EXPRESSION_EXPRESSION', 'OPTIONAL_PARAMETER_LIST'],
		[]
	],
	'EXPRESSION_EXPRESSION': [
		['ASSIGNMENT_EXPRESSION'],
	],
	'OPTIONAL_DATA_NAME_LIST': [
		['SYMBOL_COMMA__PRUNE', 'DATA_NAMES', 'OPTIONAL_DATA_NAME_LIST'],
		[]
	],
	'OPTIONAL_FUNCTION_NAME_LIST': [
		['SYMBOL_COMMA__PRUNE', 'FUNCTION_NAMES', 'OPTIONAL_FUNCTION_NAME_LIST'],
		[]
	],
	'OPTIONAL_GRANT_LIST': [
		['ACCESS_SPECIFIER', 'GRANT_LIST'],
		[]
	],
################################################################################ 11
	'ARGUMENT': [
		['TYPE', 'DATA_NAMES', 'OPTIONAL_ASSIGNMENT'],
	],
	'OPTIONAL_ARGUMENT_LIST': [
		['SYMBOL_COMMA__PRUNE', 'ARGUMENT_LIST_AFTER_FIRST'],
		[]
	],
################################################################################ Statements
	'DEFER_STATEMENT': [
		['KEYWORD_DEFER', 'SINGLE_STATEMENT_OR_CODE_BLOCK']
	],
	'DO_STATEMENT': [
		['KEYWORD_DO', 'GROUPER_LEFT_PARENTHESIS', 'EXPRESSION_EXPRESSION', 'GROUPER_RIGHT_PARENTHESIS', 'SINGLE_STATEMENT_OR_CODE_BLOCK']
	],
	'FOR_STATEMENT': [
		['KEYWORD_FOR', 'GROUPER_LEFT_PARENTHESIS', 'FOR_DATA_DECLARATION', 'EXPRESSION_EXPRESSION', 'SYMBOL_SEMICOLON__PRUNE', 'STATEMENT_LIST', 'GROUPER_RIGHT_PARENTHESIS', 'SINGLE_STATEMENT_OR_CODE_BLOCK']
	],
	'FOR_DATA_DECLARATION': [
		['DATA_DECLARATION_TYPE'],
		['SYMBOL_SEMICOLON__PRUNE']
	],
	'IF_STATEMENT': [
		['KEYWORD_IF', 'GROUPER_LEFT_PARENTHESIS', 'EXPRESSION_EXPRESSION', 'GROUPER_RIGHT_PARENTHESIS', 'SINGLE_STATEMENT_OR_CODE_BLOCK', 'ELSE_STATEMENT']
	],
	'STATIC_ELSE_STATEMENT': [
		['KEYWORD_STATICS', 'KEYWORD_ELSE', 'SINGLE_STATEMENT_OR_CODE_BLOCK'],
		[]
	],
	'STATIC_IF_STATEMENT': [
		['KEYWORD_STATICS', 'KEYWORD_IF', 'GROUPER_LEFT_PARENTHESIS', 'EXPRESSION_EXPRESSION', 'GROUPER_RIGHT_PARENTHESIS', 'SINGLE_STATEMENT_OR_CODE_BLOCK', 'STATIC_ELSE_STATEMENT']
	],
	'WHILE_STATEMENT': [
		['KEYWORD_WHILE', 'GROUPER_LEFT_PARENTHESIS', 'EXPRESSION_EXPRESSION', 'GROUPER_RIGHT_PARENTHESIS', 'SINGLE_STATEMENT_OR_CODE_BLOCK']
	],
	'CODE_BLOCK': [
		['GROUPER_LEFT_BRACE', 'STATEMENT_LIST', 'GROUPER_RIGHT_BRACE'],
	],
	'DATA_DECLARATION_LIST': [
		['TYPE', 'DATA_NAMES', 'OPTIONAL_ASSIGNMENT', 'SYMBOL_SEMICOLON__PRUNE', 'DATA_DECLARATION_LIST'],
		[]
	],
	'GOTO_STATEMENT': [
		['KEYWORD_GOTO', 'DATA_NAMES']
	],
	'HACK_STATEMENT': [
		['KEYWORD_HACK', 'GROUPER_LEFT_PARENTHESIS', 'PARAMETER_LIST', 'GROUPER_RIGHT_PARENTHESIS']
	],
	'ITER_STATEMENT': [
		['SYMBOL_PLUS__PLUS', 'EXPRESSION_EXPRESSION'],
		['SYMBOL_MINUS__MINUS', 'EXPRESSION_EXPRESSION'],
	],
	'LABEL_STATEMENT': [
		['KEYWORD_LABEL', 'DATA_NAMES']
	],
	'RETURN_STATEMENT': [
		['KEYWORD_RETURN', 'PARAMETER_LIST'],
	],
	'OPTIONAL_PARAMETER_LIST': [
		['SYMBOL_COMMA__PRUNE', 'PARAMETER_LIST'],
		[]
	],
	'ASSIGNMENT_EXPRESSION': [
		['OR_EXPRESSION', 'OPTIONAL_ASSIGNMENT_EXPRESSION']
	],
################################################################################ 12
	'ARGUMENT_LIST_AFTER_FIRST': [
		['TYPE', 'DATA_NAMES', 'OPTIONAL_ASSIGNMENT', 'OPTIONAL_ARGUMENT_LIST', 'OPTIONAL_ARGUMENT_LIST'],
		#['IDENTIFIER_VARIABLE', 'OPTIONAL_ARGUMENT_LIST', 'OPTIONAL_ARGUMENT_LIST'],
		[],
	],
	'SINGLE_STATEMENT_OR_CODE_BLOCK': [
		['STATEMENT', 'SYMBOL_SEMICOLON__PRUNE'],
		['NO_SEMICOLON_STATEMENT'],
	],
	'ELSE_STATEMENT': [
		['KEYWORD_ELSE', 'SINGLE_STATEMENT_OR_CODE_BLOCK'],
		[]
	],
################################################################################ 13
# EXPRESSION BLOCK.
# Contains all valid expressions in the language. These are sums, == compares...
# a + b * c - d
################################################################################
################################################################################
	'OR_EXPRESSION': [
		['AND_EXPRESSION', 'OPTIONAL_OR_EXPRESSION'],
	],
	'OPTIONAL_ASSIGNMENT_EXPRESSION': [
		['SYMBOL_EQUAL', 'OR_EXPRESSION'],
		['SYMBOL_FORWARD_SLASH__EQUAL', 'OR_EXPRESSION'],
		['SYMBOL_MINUS__EQUAL', 'OR_EXPRESSION'],
		['SYMBOL_PLUS__EQUAL', 'OR_EXPRESSION'],
		['SYMBOL_STAR__EQUAL', 'OR_EXPRESSION'],
		[]
	],
################################################################################ 14
	'AND_EXPRESSION': [
		['BITWISE_OR_EXPRESSION', 'OPTIONAL_AND_EXPRESSION'],
	],
	'OPTIONAL_OR_EXPRESSION': [
		['SYMBOL_BAR__BAR', 'OR_EXPRESSION'],
		[]
	],
################################################################################ 15
	'BITWISE_OR_EXPRESSION': [
		['BITWISE_XOR_EXPRESSION', 'OPTIONAL_BITWISE_OR_EXPRESSION'],
	],
	'OPTIONAL_AND_EXPRESSION': [
		['SYMBOL_AMPERSAND__AMPERSAND', 'AND_EXPRESSION'],
		[]
	],
################################################################################ 16
	'BITWISE_XOR_EXPRESSION': [
		['BITWISE_AND_EXPRESSION', 'OPTIONAL_BITWISE_XOR_EXPRESSION'],
	],
	'OPTIONAL_BITWISE_OR_EXPRESSION': [
		['SYMBOL_BAR', 'BITWISE_OR_EXPRESSION'],
		[]
	],
################################################################################ 17
	'BITWISE_AND_EXPRESSION': [
		['EQUALITY_EXPRESSION', 'OPTIONAL_BITWISE_AND_EXPRESSION'],
	],
	'OPTIONAL_BITWISE_XOR_EXPRESSION': [
		['SYMBOL_CARET', 'BITWISE_XOR_EXPRESSION'],
		[]
	],
################################################################################ 18
	'EQUALITY_EXPRESSION': [
		['RELATIONAL_EXPRESSION', 'OPTIONAL_EQUALITY_EXPRESSION'],
	],
	'OPTIONAL_BITWISE_AND_EXPRESSION': [
		['SYMBOL_AMPERSAND', 'BITWISE_AND_EXPRESSION'],
		[]
	],
################################################################################ 19
	'RELATIONAL_EXPRESSION': [
		['ADDITIVE_EXPRESSION', 'OPTIONAL_RELATIONAL_EXPRESSION'],
	],
	'OPTIONAL_EQUALITY_EXPRESSION': [
		['SYMBOL_EQUAL__EQUAL', 'EQUALITY_EXPRESSION'],
		[]
	],
################################################################################ 20
	'ADDITIVE_EXPRESSION': [
		['MULTIPLICATIVE_EXPRESSION', 'OPTIONAL_ADDITIVE_EXPRESSION'],
	],
	'OPTIONAL_RELATIONAL_EXPRESSION': [
		['RELATIONAL_OPERATOR', 'EQUALITY_EXPRESSION'],
		[]
	],
################################################################################ 21
	'MULTIPLICATIVE_EXPRESSION': [
		['CAST_EXPRESSION', 'OPTIONAL_MULTIPLICATIVE_EXPRESSION'],
	],
	'OPTIONAL_ADDITIVE_EXPRESSION': [
		['SYMBOL_MINUS', 'ADDITIVE_EXPRESSION'],
		['SYMBOL_PLUS', 'ADDITIVE_EXPRESSION'],
		[]
	],
	'RELATIONAL_OPERATOR': [
		['SYMBOL_LESS_THAN'],
		['SYMBOL_GREATER_THAN'],
		['SYMBOL_LESS_THAN__EQUAL'],
		['SYMBOL_GREATER_THAN__EQUAL'],
	],
################################################################################ 22
	'OPTIONAL_MULTIPLICATIVE_EXPRESSION': [
		['SYMBOL_FORWARD_SLASH', 'MULTIPLICATIVE_EXPRESSION'],
		['SYMBOL_STAR', 'MULTIPLICATIVE_EXPRESSION'],
		[]
	],
	'CAST_EXPRESSION': [
		['KEYWORD_CAST', 'GROUPER_LEFT_BRACKET', 'TYPE', 'GROUPER_RIGHT_BRACKET', 'GROUPER_LEFT_PARENTHESIS', 'EXPRESSION_EXPRESSION', 'GROUPER_RIGHT_PARENTHESIS'],
		['NEW_EXPRESSION'],
	],
################################################################################ 23
	'NEW_EXPRESSION': [
		['KEYWORD_NEW', 'GROUPER_LEFT_BRACKET', 'TYPE', 'GROUPER_RIGHT_BRACKET', 'OPTIONAL_NEW_LIST', 'OPTIONAL_CONSTRUCTOR_LIST'],
		['DELETE_EXPRESSION'],
	],
################################################################################ 23.1
	'DELETE_EXPRESSION': [
		['KEYWORD_DELETE', 'GROUPER_LEFT_PARENTHESIS', 'EXPRESSION_EXPRESSION', 'GROUPER_RIGHT_PARENTHESIS'],
		['UNARY_EXPRESSION'],
	],
	'OPTIONAL_NEW_LIST': [
		['GROUPER_LEFT_PARENTHESIS', 'EXPRESSION_EXPRESSION', 'OPTIONAL_EXPRESSION', 'GROUPER_RIGHT_PARENTHESIS'],
		[]
	],
	'OPTIONAL_CONSTRUCTOR_LIST': [
		['GROUPER_LEFT_BRACE', 'PARAMETER_LIST', 'GROUPER_RIGHT_BRACE'],
		[]
	],
################################################################################ 23.3
	'UNARY_EXPRESSION': [
		['MEMBER_EXPRESSION'],
		['UNARY_OPERATOR', 'CAST_EXPRESSION'],
	],
	'OPTIONAL_EXPRESSION': [
		['SYMBOL_COMMA__PRUNE', 'EXPRESSION_EXPRESSION'],
		[]
	],
################################################################################ 24
	'MEMBER_EXPRESSION': [
		['IDENTIFIER_CLASS', 'CLASS_MEMBER_EXPRESSION'],
		['IDENTIFIER_ENUMERATION', 'ENUMERATION_MEMBER_EXPRESSION'],
		['IDENTIFIER_PACKAGE', 'OPTIONAL_MEMBER_EXPRESSION'],
		['IDENTIFIER_VARIABLE', 'OPTIONAL_MEMBER_EXPRESSION'],
		['IDENTIFIER_SUBROUTINE', 'OPTIONAL_MEMBER_EXPRESSION'],
		['RESOURCE', 'OPTIONAL_MEMBER_EXPRESSION'],
	],
	'UNARY_OPERATOR': [
		['SYMBOL_APETAIL'],
		['SYMBOL_APETAIL__APETAIL'],
		['SYMBOL_DOLLAR'],
		['SYMBOL_DOLLAR__DOLLAR'],
		['SYMBOL_EXCLAMATION_MARK'],
		['SYMBOL_EXCLAMATION_MARK__EXCLAMATION_MARK'],
		['SYMBOL_MINUS'],
	],
################################################################################ 25
	'CLASS_MEMBER_EXPRESSION': [
		['GROUPER_LEFT_PARENTHESIS', 'PARAMETER_LIST', 'GROUPER_RIGHT_PARENTHESIS'],
		['SYMBOL_DOT__PRUNE', 'CLASS_MEMBER', 'OPTIONAL_MEMBER_EXPRESSION'],
	],
	'ENUMERATION_MEMBER_EXPRESSION': [
		['SYMBOL_DOT__PRUNE', 'IDENTIFIER_VARIABLE'],
		[]
	],
	'RESOURCE': [
		['INTEGER_LITERAL'],
		['GROUPER_LEFT_PARENTHESIS', 'EXPRESSION_EXPRESSION', 'GROUPER_RIGHT_PARENTHESIS'],
		['GROUPER_LEFT_BRACKET', 'EXPRESSION_LIST', 'GROUPER_RIGHT_BRACKET'],
		['STRING'],
		['WHEN_EXPRESSION'],
		['KEYWORD_LAMBDA', 'OPTIONAL_CAPTURE_LIST', 'FUNCTION_SIGNATURE', 'CODE_BLOCK']
	],
	'OPTIONAL_MEMBER_EXPRESSION': [
		['ARRAY_ACCESS_EXPRESSION'],
		['GROUPER_LEFT_PARENTHESIS', 'PARAMETER_LIST', 'GROUPER_RIGHT_PARENTHESIS', 'OPTIONAL_EXTRACTOR_EXPRESSION'],
		['SYMBOL_DOT__PRUNE', 'MEMBER_EXPRESSION'],
		[]
	],
################################################################################ 26
	'CLASS_MEMBER': [
		['IDENTIFIER_SUBROUTINE'],
		['IDENTIFIER_VARIABLE'],
		['IDENTIFIER_PACKAGE']
	],
	'EXPRESSION_LIST': [
		['EXPRESSION_EXPRESSION', 'EXPRESSION_LIST'],
		['SYMBOL_COMMA__PRUNE', 'EXPRESSION_LIST'],
		[]
	],
	'WHEN_EXPRESSION': [
		['KEYWORD_WHEN', 'GROUPER_LEFT_PARENTHESIS', 'OR_EXPRESSION', 'GROUPER_RIGHT_PARENTHESIS', 'OR_EXPRESSION', 'KEYWORD_ELSE', 'OR_EXPRESSION'],
	],
	'CAPTURE_LIST': [
		['UNARY_OPERATOR', 'DATA_NAMES', 'CAPTURE_LIST'],
		['DATA_NAMES', 'CAPTURE_LIST'],
		[]
	],
	'OPTIONAL_EXTRACTOR_EXPRESSION': [
		['SYMBOL_TILDE__PRUNE', 'DATA_NAMES', 'OPTIONAL_MEMBER_EXPRESSION'],
		[]
	],
	'OPTIONAL_CAPTURE_LIST': [
		['GROUPER_LEFT_BRACKET', 'CAPTURE_LIST', 'GROUPER_RIGHT_BRACKET'],
		[]
	],
	'ARRAY_ACCESS_EXPRESSION': [
		['GROUPER_LEFT_BRACKET', 'EXPRESSION_EXPRESSION', 'OPTIONAL_ARRAY_ACCESS_EXPRESSION', 'GROUPER_RIGHT_BRACKET', 'OPTIONAL_MEMBER_EXPRESSION']
	],
################################################################################ 27
	'OPTIONAL_ARRAY_ACCESS_EXPRESSION': [
		['SYMBOL_COMMA__PRUNE', 'EXPRESSION_EXPRESSION', 'OPTIONAL_ARRAY_ACCESS_EXPRESSION'],
		[]
	]
################################################################################
################################################################################
################################################################################
}
