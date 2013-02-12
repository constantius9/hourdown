# hourdown #

Obscure time management tool with timeslots and automatic assignment (in future).

## TODO ##

1. `[ ]` Add support of time budget.
	1. `[ ]` Define the notion of timeslot. Handle the slots factoring of continuos time.
		* Slots in day time basically work a bit like fields in C structure:
			* Their size can be specified, like for bitfields.
			* They are aligned. Although, alignment rules are not the same. It's not required to align all activities on the boundary of tha longest one, but some alignment should certainly happen to account for context switch and associated loss of time. This way, specific context switch times should not be planned for (like preparation for the commute from work to home, which includes finishing work, turning computer off, organizing stuff on the work table, saying goodbye to team, putting coat and boots on and exiting the building).
		* Time budget should deal with timeslots and possible factorizations of day into different amount of timeslots, considering necessary alignment. Say, factoring 17-hour day into 2-hour slots will leave you with 16 effective hours and 1 hour padding. This one hour padding may seem like excessive and strange to account for, but I believe it can effectively simulate time loss of context switches between 2-hour slots. Although, the problem of different context switch times with different slot size occurs. It actually should work in such a way that having a lot of small slots is going to be ineffective due to a lot of context switch losses.
		* There should be different strategies of day-slot factorization. Like, `2h×2:1h×4:30m×8:15m×16` gives us 16 hours in 30 slots of different sizes.
		* There should be tasks and appointments.
			* Tasks contribute to some project and don't necessarily mean finish of the project on completion of all tasks. 
			* Appoinments appear at fixed points in time and are necessarily finished, although sometimes end time is not specified. Examples:
				* Training at work may be scheduled in the form of `1PM:3PM`, which gives us 2-hour long fixed appointment. It will most likely finish around 3PM.
				* Meeting with friends may be scheduled in the form of `4PM:?`, which gives us a non-fixed appoinment, meaning we're not sure when we'll go home.
		* There should be different strategies of slot choice. When a task is added, some possible execution time should be chosen automatically with possible customization.
		* Factorization may be fixed or floating. Fixed factorization means it can't be re-done after being done, floating is the opposite.
1. `[ ]` Add support of offline project description using syntax, similar to syntax of this document.
	* It's basically Markdown with some specific extensions.
	* Tasks are marked with \`[ ]\`.
	* They're organized into ordered hierarchic lists with `1.`'s.
