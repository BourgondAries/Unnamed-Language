// Copyright © 2015 Kevin Robert Stravers
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
#include "CommentFilter.hpp"

namespace tul { namespace filter {

void CommentFilter::push(char symbol)
{
	comment_buffer.putCharInto(symbol);
	symbols_waiting = comment_ignorer.putOnStack(symbol);
}

bool CommentFilter::available() const
{
	return symbols_waiting > 0;
}

char CommentFilter::pop()
{
	return comment_buffer.getCharFrom(symbols_waiting--);
}

}}