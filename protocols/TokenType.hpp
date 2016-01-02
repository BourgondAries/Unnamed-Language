// Copyright © 2015-2016 Kevin Robert Stravers
/*
This file is part of Cxy Compiler Reference Implementation (Cxy CRI).

Cxy CRI is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Cxy CRI is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Cxy CRI.  If not, see <http://www.gnu.org/licenses/>.
*/
#pragma once

namespace tul { namespace protocols { 

enum class TokenType
{
	END_OF_MODULE,
	GROUPER_LEFT_BRACE,
	GROUPER_LEFT_BRACKET,
	GROUPER_LEFT_PARENTHESIS,
	GROUPER_RIGHT_BRACE,
	GROUPER_RIGHT_BRACKET,
	GROUPER_RIGHT_PARENTHESIS,
	IDENTIFIER_CLASS,
	IDENTIFIER_CONSTEXPR,
	IDENTIFIER_ENUMERATION,
	IDENTIFIER_PACKAGE,
	IDENTIFIER_SUBROUTINE,
	IDENTIFIER_VARIABLE,
	INTEGER_LITERAL,
	KEYWORD_BREAK,
	KEYWORD_CAST,
	KEYWORD_CATCH,
	KEYWORD_CONST,
	KEYWORD_CONSTRUCT,
	KEYWORD_CONSTRUCTOR,
	KEYWORD_CONTINUE,
	KEYWORD_DEBUG,
	KEYWORD_DEFER,
	KEYWORD_DELETE,
	KEYWORD_DESTRUCTOR,
	KEYWORD_DO,
	KEYWORD_DOUBLE,
	KEYWORD_ELSE,
	KEYWORD_ENUM,
	KEYWORD_EXPERIMENTAL,
	KEYWORD_FLOAT,
	KEYWORD_FOR,
	KEYWORD_FOREACH,
	KEYWORD_GOTO,
	KEYWORD_HACK,
	KEYWORD_IF,
	KEYWORD_IN,
	KEYWORD_LABEL,
	KEYWORD_LAMBDA,
	KEYWORD_NEW,
	KEYWORD_PRIVATE,
	KEYWORD_PTR,
	KEYWORD_PUBLIC,
	KEYWORD_PURE,
	KEYWORD_REF,
	KEYWORD_RESTRICTED,
	KEYWORD_RETURN,
	KEYWORD_SIZE,
	KEYWORD_STATIC,
	KEYWORD_THIS,
	KEYWORD_THROW,
	KEYWORD_TRY,
	KEYWORD_TYPE,
	KEYWORD_VAR,
	KEYWORD_WHEN,
	KEYWORD_WHILE,
	PRIMITIVE_SIGNED,
	PRIMITIVE_SIGNED_WRAPPED,
	PRIMITIVE_UNSIGNED,
	PRIMITIVE_UNSIGNED_WRAPPED,
	STRING,
	SYMBOL_AMPERSAND,
	SYMBOL_AMPERSAND__AMPERSAND,
	SYMBOL_AMPERSAND__AMPERSAND__EQUAL,
	SYMBOL_AMPERSAND__EQUAL,
	SYMBOL_APETAIL,
	SYMBOL_BAR,
	SYMBOL_BAR__BAR,
	SYMBOL_BAR__BAR__EQUAL,
	SYMBOL_BAR__EQUAL,
	SYMBOL_CARET,
	SYMBOL_CARET__EQUAL,
	SYMBOL_COLON,
	SYMBOL_COMMA,
	SYMBOL_DOLLAR,
	SYMBOL_DOLLAR__DOLLAR,
	SYMBOL_DOT,
	SYMBOL_EQUAL,
	SYMBOL_EQUAL__EQUAL,
	SYMBOL_EXCLAMATION_MARK,
	SYMBOL_EXCLAMATION_MARK__EQUAL,
	SYMBOL_EXCLAMATION_MARK__EXCLAMATION_MARK,
	SYMBOL_EXCLAMATION_MARK__EXCLAMATION_MARK__EQUAL,
	SYMBOL_FORWARD_SLASH,
	SYMBOL_FORWARD_SLASH__EQUAL,
	SYMBOL_GREATER_THAN,
	SYMBOL_GREATER_THAN__EQUAL,
	SYMBOL_GREATER_THAN__GREATER_THAN,
	SYMBOL_GREATER_THAN__GREATER_THAN__EQUAL,
	SYMBOL_LESS_THAN,
	SYMBOL_LESS_THAN__EQUAL,
	SYMBOL_LESS_THAN__LESS_THAN,
	SYMBOL_LESS_THAN__LESS_THAN__EQUAL,
	SYMBOL_MINUS,
	SYMBOL_MINUS__EQUAL,
	SYMBOL_MINUS__GREATER_THAN,
	SYMBOL_MINUS__MINUS,
	SYMBOL_PERCENT,
	SYMBOL_PERCENT__EQUAL,
	SYMBOL_PLUS,
	SYMBOL_PLUS__EQUAL,
	SYMBOL_PLUS__PLUS,
	SYMBOL_SEMICOLON,
	SYMBOL_STAR,
	SYMBOL_STAR__EQUAL,
	SYMBOL_TILDE,
	UNIDENTIFIED,
	ENUM_END
};

}}
