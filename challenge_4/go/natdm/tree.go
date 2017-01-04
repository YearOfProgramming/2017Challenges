package natdm

import (
	"context"
	"encoding/json"
	"fmt"
	"log"
	"time"
)

var key string

func reverse(t *tree, to time.Duration) error {
	// Add five second timeout so trees don't infinitely reverse, if it's a big enough tree
	ctx, cancel := context.WithTimeout(context.Background(), to)
	defer cancel()

	// If the timeout is hit, stop reversing the tree
	select {
	case <-t.reverse(ctx):
		return nil
	case <-ctx.Done():
		return fmt.Errorf("could not finish before %s", to.String())
	}
}

func main() {
	t := &tree{
		A: &tree{
			A: &tree{
				V: 4,
			},
			B: &tree{
				V: 2,
				A: &tree{
					V: 100,
					A: &tree{
						V: 94,
					}, B: &tree{
						V: 66,
					},
				},
				B: &tree{},
			},
			V: 10,
		},
		B: &tree{
			A: &tree{
				V: 12,
			},
			B: &tree{
				V: 5,
			},
			V: 90,
		},
		V: 9,
	}

	// Add five second timeout so trees don't infinitely reverse, if it's a big enough tree
	ctx, cancel := context.WithTimeout(context.Background(), time.Second*5)
	defer cancel()

	// If the timeout is hit, stop reversing the tree
	select {
	case <-t.reverse(ctx):
		log.Println(t)
	case <-ctx.Done():
		log.Println("could not finish")
	}
}

type tree struct {
	A *tree `json:"a"`
	B *tree `json:"b"`
	V int   `json:"val"`
}

func (t *tree) String() string {
	bs, _ := json.MarshalIndent(t, "", "\t")
	return string(bs)
}

func (t *tree) reverse(ctx context.Context) <-chan struct{} {
	done := make(chan struct{})
	go func() {
		defer close(done)

		if t.A != nil && t.B != nil {
			i := t.A
			t.A = t.B
			t.B = i

			var x bool
			for {
				select {
				case <-t.A.reverse(ctx):
					if x {
						done <- struct{}{}
						break
					} else {
						x = true
					}
				case <-t.B.reverse(ctx):
					if x {
						done <- struct{}{}
						break
					} else {
						x = true
					}
				case <-ctx.Done():
					done <- struct{}{}
					break
				}
			}
		}
	}()
	return done
}
