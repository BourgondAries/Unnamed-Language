// Copyright © 2015 Kevin Robert Stravers
/*
This file is part of Unnamed-Language Compiler Reference Implementation (ULCRI).

ULCRI is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

ULCRI is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with ULCRI.  If not, see <http://www.gnu.org/licenses/>.
*/
#include "CommentIgnorer.hpp"

#include <iostream>


namespace tul { namespace dependency {

CommentIgnorer::CommentIgnorer()
:
  comment_state(State::NO_COMMENT)
{}


uint8_t CommentIgnorer::putOnStack(char character_)
{
  switch (comment_state)
  {
    case State::NO_COMMENT:
    {
      switch (character_)
      {
        case '/': comment_state = State::ONE_SLASH; break;
        case '"': comment_state = State::INSIDE_QUOTE; return 1; break;
        default: return 1; break;
      }
    }
    break;

    case State::ONE_SLASH:
    {
      switch (character_)
      {
        case '/': comment_state = State::LINE_COMMENT; break;
        case '*': comment_state = State::BLOCK_COMMENT; ++block_nest; break;
        default: comment_state = State::NO_COMMENT; return 2; break;
      }
    }
    break;
    case State::INSIDE_QUOTE:
      switch (character_)
      {
        case '"': comment_state = State::MAYBE_OUTQUOTE; return 1; break;
        default: return 1; break;
      }
    break;

    case State::LINE_COMMENT:
      switch (character_)
      {
        case '\n': comment_state = State::NO_COMMENT; return 1; break;
        default: break;
      }
    break;
		case State::BLOCK_COMMENT:
			switch (character_)
			{
				case '*': comment_state = State::ONE_STAR; break;
				default: break;	
			}
    break;
    case State::MAYBE_OUTQUOTE:
      switch (character_)
      {
        case '"': comment_state = State::INSIDE_QUOTE; return 1; break;
        default: comment_state = State::NO_COMMENT; return 1; break;
      }
    break;

    case State::ONE_STAR:
      switch (character_)
      {
        case '/': comment_state = --block_nest == 0 ? State::NO_COMMENT : State::BLOCK_COMMENT;
        break;
        case '*': break;
        default: comment_state = State::BLOCK_COMMENT; break;
      }
    break;
    default: break;
  }

  return 0;
}

}}
